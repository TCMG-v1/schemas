import json
from pathlib import Path

def build_workspace_packet(task, project_root, tools, round_state):
    # TODO: plug in your dnd-context-compressor here
    context_summaries = []  # list of {path, summary, content_ref}
    return {
        "task": task,
        "project_context": context_summaries,
        "available_tools": tools,
        "round_state": round_state,
    }

def log_round_result(result, log_dir="logs"):
    Path(log_dir).mkdir(exist_ok=True)
    out = Path(log_dir) / f"{result['round_id']}.json"
    out.write_text(json.dumps(result, indent=2))
