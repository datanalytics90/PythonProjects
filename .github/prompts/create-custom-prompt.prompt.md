---
mode: 'agent'
description: 'Create a reusable VS Code Copilot prompt file from a repeatable task pattern'
tools: ['codebase', 'editFiles', 'search', 'terminal']
---

# Create a reusable prompt

You are helping turn a repeatable workflow into a reusable custom prompt for VS Code Copilot Chat.

## Goal
Create a polished .prompt.md file that captures the task pattern clearly and makes it easy to reuse.

## Before drafting
Identify the following if they are not already provided:
- The core task being repeated
- The expected inputs such as selected code, files, project type, or environment
- The desired output format or tone
- Whether the prompt should be workspace-scoped or broadly reusable

## Instructions
1. Summarize the task pattern in a concise and actionable way.
2. Write the prompt so it is specific enough to be useful but flexible enough to support variations.
3. Include:
   - a clear objective
   - relevant context or inputs
   - step-by-step guidance
   - success criteria or expected output
   - any constraints or style requirements
4. Prefer short, direct instructions over vague wording.
5. If the task pattern is unclear, ask one or two focused clarifying questions before drafting.

## Output format
Return:
- a ready-to-save prompt draft
- a suggested filename such as task-name.prompt.md
- a short explanation of what the prompt is designed to do

## Quality bar
- Make the instructions easy to follow.
- Avoid filler and ambiguity.
- Use placeholders only when they improve clarity.
- Favor practical, reusable wording over generic advice.
