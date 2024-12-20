from src.app import App

def main():
    app = App()

    while(True):
        command = input('Enter command: [1 : register] [2 : check-in] [3 : check-out] [q : quit] \n')

        if command == 'q':
            print('GOODBYE!! SAD TO SEE YOU LEAVE :(')
            break

        while command == '1':
            # REGISTER USER
            first_name = input('Enter first name: ')

            if first_name == '':
                print('Empty name not allowed, input name again')
                continue

            last_name = input('Enter last name: ')
            phone = input('Enter phone: ')

            app.register_person(first_name, last_name, phone)
            break
        if command == '2':
            # CHECK IN 
            app.check_in()
        elif command == '3':
            # CHECK OUT
            app.check_out()

    app.camera.close()
        
if __name__ == "__main__":
    main()


# class Node:
#     def __init__(self):
#         self.sum = 0
#         self.l = 0 #LEFT_BOUND
#         self.r = 0 #RIGHT_BOUND
#         self.lChild = None
#         self.rChild = None

# class SegTree:
#     def __init__(self, n):
#         self.n = n
#         self.root = Node()
#         self.build(self.root, 0, n - 1)

#     def build(self, node, left, right):
#         node.l = left
#         node.r = right

#         if left == right:
#             return node

#         mid = left + (right - left) // 2
#         lChild = self.build(Node(), left, mid)
#         rChild = self.build(Node(), mid + 1, right)

#         node.sum = lChild.sum + rChild.sum
#         return node

#     def range_sum(self, left, right):
#         return self.range(self.root, left, right)

#     def rangeQ(self, node, left ,right):
#         if right < node.l or left > node.r:
#             return 0
#         if left <= node.l and right >= node.r:
#             return node.sum
        
#         return self.rangeQ(node.lChild, left, right) + self.rangeQ(node.rChild, left, right)

#     def update(self, index, val):
#         self.pointUpdate(self.root, index, val)

#     def pointUpdate(self, node, index, value):
#         if node.l == node.r == index:
#             node.sum = value
#             return
        
#         if index <= node.lChild.r:
#             self.pointUpdate(node.lChild, index, value)
#         else:
#             self.pointUpdate(node.rChild, index, value)

#         node.sum = node.lChild.sum + node.rChild.sum
