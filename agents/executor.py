class ExecutorAgent:
    def __init__(self, tool_registry):
        self.tool_registry = tool_registry
        self.context = {}

    def execute(self, plan):
        execution_log = []

        for action in plan.actions:
            tool = self.tool_registry.get(action.type)

            # RULE 1: Unknown action
            if not tool:
                if action.required:
                    raise RuntimeError(
                        f"Required tool '{action.type}' not registered"
                    )
                else:
                    continue

            # RULE 2: Gather required inputs
            inputs = {}
            for key in tool.required_inputs:
                if key not in self.context:
                    if action.required:
                        raise RuntimeError(
                            f"Missing required input '{key}' for action '{action.type}'"
                        )
                    else:
                        continue
                inputs[key] = self.context[key]

            # RULE 3: Execute tool
            result = tool.execute(**inputs)

            # Store output deterministically
            self.context[action.type] = result
            execution_log.append({action.type: result})

        return execution_log
