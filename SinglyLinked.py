#Python program to search an element in Singly Linked List

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

#creating linked list class
class SinglyLinkedList:
  def __init__(self):
    self.head = None

  #Adding new element at the end of the list
  def push_back(self, newElement):
    newNode = Node(newElement)
    if(self.head == None):
      self.head = newNode
      return
    else:
      temp = self.head
      while(temp.next != None):
        temp = temp.next
      temp.next = newNode

  #Searching the element
  def Search(self, ele):
    temp = self.head
    found = 0
    i = 0 

    if(temp != None):
      while (temp != None):
        i += 1
        if(temp.data == ele):
          found += 1
          break
        temp = temp.next
      if(found == 1):
        print(ele,"is found at position =", i)
      else:
        print(ele,"is not found in the given linked list.")
    else:
      print("The list is empty.")

  #to display the elements of the list
  def show(self):
    temp = self.head
    if(temp != None):
      print("The list elements are:", end=" ")
      while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
      print()
    else:
      print("The list is empty.")

                 
s = SinglyLinkedList()

print("press 1 to add element to the linked list")
print("press 0 to stop adding the element to the list")
n=10
#Add elements into the linkedlist.
while(n!=0):
    print("press 1 to add element to the linked list")
    print("press 0 to stop adding the element to the list")
    n=int(input("Enter your choice : "))
    if(n==1):
        s.push_back(int(input("Enter element to add : ")))

    elif(n==0):
        break
    else:
        print("[INVALID INPUT]: try again")
        continue
      
#display the elements of the list.
key = int(input("enter the element to search  into the linked list"))

s.show()
#searching the element in the list
s.Search(key)
