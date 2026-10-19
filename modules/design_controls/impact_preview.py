"""Impact preview: before a design change is approved, show which DHF outputs, risk controls and cleared devices it
touches, and whether it is likely to need a Special 510(k), with no tracing by hand (simulated)."""


def preview(trace_result: dict, cleared_devices: dict) -> dict:
    devices = sorted(d for d, outputs in cleared_devices.items() if set(outputs) & set(trace_result.get("design_outputs", [])))
    return {"design_outputs": trace_result.get("design_outputs", []), "risk_controls": trace_result.get("risk_controls", []),
            "cleared_devices": devices, "special_510k_likely": bool(devices)}
