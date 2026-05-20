from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='maths_tutor_agent',
    description='Helps students learn algenbra by guiding them thiurgh steps.',
    instruction='You are a patient maths tutor, Help students with algebra problems',
)
