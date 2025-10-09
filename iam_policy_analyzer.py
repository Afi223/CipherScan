class IAMPolicyAnalyzer:
    """
    Analyzes IAM policy JSON documents for risky configurations,
    such as wildcard permissions or overly broad resource access.
    """

    @staticmethod
    def analyze_policy(policy):
        """
        Analyze an IAM policy dictionary and return a list of security issues.

        Args:
            policy (dict): IAM policy JSON object.

        Returns:
            list[str]: Findings or "Policy is secure!" if none found.
        """
        issues = []

        for statement in policy.get('Statement', []):
            # Normalize 'Action' and 'Resource' to lists for consistent handling
            actions = statement.get('Action', [])
            resources = statement.get('Resource', [])
            effect = statement.get('Effect', 'Unknown')

            if isinstance(actions, str):
                actions = [actions]
            if isinstance(resources, str):
                resources = [resources]

            # Detect wildcard actions for S3 (e.g., s3:*)
            for action in actions:
                if action.lower().startswith("s3:") and "*" in action:
                    issues.append(" Wildcard permission detected: s3:*")

            # Detect overly broad 'Allow' with wildcard resource
            if effect == "Allow" and any(r == "*" for r in resources):
                issues.append(" Overly broad resource access detected ('*').")

        return issues if issues else [" Policy is secure!"]
