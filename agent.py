class Agent:
    def __init__(self, vision_module, asr_module):
        self.vision = vision_module
        self.asr = asr_module

    def start_interaction(self):
        # Step 1: Recognize face and greet the user
        user_info = self.vision.recognize_face()
        if user_info:
            print(f"Xin chào {user_info['name']}, tôi có thể giúp gì cho bạn hôm nay?")

        # Step 2: Listen to the user's needs
        user_input = self.asr.listen_and_recognize()
        print(f"User said: {user_input}")

        # Step 3: Provide consultation or open account
        if "tư vấn" in user_input.lower():
            self.provide_consultation(user_info)
        elif "mở tài khoản" in user_input.lower():
            self.open_account()

    def provide_consultation(self, user_info):
        # Retrieve and suggest products based on user information
        products = self.retrieve_suggestions(user_info)
        self.display_products(products)

    def open_account(self):
        # Proceed with account opening process
        print("Hãy quét CMND/CCCD của bạn...")
        # Include further steps such as biometric validation, etc.

    def retrieve_suggestions(self, user_info):
        # Logic to retrieve financial products based on user data
        return ["Gói tiết kiệm A", "Gói tiết kiệm B"]

    def display_products(self, products):
        for product in products:
            print(f"Gói sản phẩm: {product}")
            # Implement display logic
