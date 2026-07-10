const form        = document.getElementById("predictForm");
const submitBtn   = document.getElementById("submitBtn");
const btnText     = document.getElementById("btnText");
const btnSpinner  = document.getElementById("btnSpinner");
const idleState   = document.getElementById("idleState");
const resultState = document.getElementById("resultState");
const resetBtn    = document.getElementById("resetBtn");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const fd = new FormData(form);
  const payload = {
    gender:            fd.get("gender"),
    age:               parseFloat(fd.get("age")),
    hypertension:      parseInt(fd.get("hypertension")),
    heart_disease:     parseInt(fd.get("heart_disease")),
    ever_married:      fd.get("ever_married"),
    work_type:         fd.get("work_type"),
    Residence_type:    fd.get("Residence_type"),
    avg_glucose_level: parseFloat(fd.get("avg_glucose_level")),
    bmi:               parseFloat(fd.get("bmi")),
    smoking_status:    fd.get("smoking_status"),
  };

  setLoading(true);

  try {
    const resp = await fetch("/predict", {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify(payload),
    });

    if (!resp.ok) {
      const err = await resp.json();
      throw new Error(err.detail || "Server error");
    }

    const result = await resp.json();
    showResult(result, payload);

  } catch (err) {
    alert("Error: " + err.message);
  } finally {
    setLoading(false);
  }
});

function showResult(result, payload) {
  idleState.classList.add("hidden");
  resultState.classList.remove("hidden");

  const isStroke  = result.prediction === 1;
  const riskLevel = result.risk_level ?? "Low Risk";

  // Icon
  document.getElementById("verdictIcon").textContent = isStroke ? "⚠️" : "✅";

  // Verdict badge
  const badge = document.getElementById("verdictBadge");
  badge.textContent = result.class_name;
  badge.className = "verdict-badge " + (isStroke ? "verdict-stroke" : "verdict-no-stroke");

  // Risk tag
  const tag = document.getElementById("riskTag");
  tag.textContent = riskLevel;
  tag.className = "risk-tag " + (
    riskLevel === "High Risk"     ? "risk-high"     :
    riskLevel === "Moderate Risk" ? "risk-moderate" : "risk-low"
  );

  // Breakdown
  document.getElementById("breakdown").innerHTML = [
    { label: "Age",           value: payload.age + " yrs" },
    { label: "Gender",        value: payload.gender },
    { label: "Hypertension",  value: payload.hypertension  === 1 ? "Yes" : "No" },
    { label: "Heart Disease", value: payload.heart_disease === 1 ? "Yes" : "No" },
    { label: "Avg Glucose",   value: payload.avg_glucose_level + " mg/dL" },
    { label: "BMI",           value: payload.bmi },
    { label: "Smoking",       value: payload.smoking_status },
    { label: "Work Type",     value: payload.work_type },
  ].map(i => `
    <div class="bd-item">
      <span class="bd-label">${i.label}</span>
      <span class="bd-value">${i.value}</span>
    </div>`
  ).join("");
}

resetBtn.addEventListener("click", () => {
  form.reset();
  resultState.classList.add("hidden");
  idleState.classList.remove("hidden");
});
function setLoading(on) {
  submitBtn.disabled = on;
  btnText.textContent = on ? "Analysing..." : "Analyse Risk";
  btnSpinner.classList.toggle("hidden", !on);
}
