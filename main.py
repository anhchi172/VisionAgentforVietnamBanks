from vision_module import VisionModule
from asr_module import ASRModule
from vision_ouput import VisualOutput
from agent import Agent
def main():
    vision = VisionModule()
    asr = ASRModule()
    agent = Agent(vision, asr)
    visual_output = VisualOutput()

    agent.start_interaction()

if __name__ == "__main__":
    main()
