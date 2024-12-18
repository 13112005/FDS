#include <iostream>
#define MAX 10

Class Deque {
Private:
    Int arr[MAX];
    Int front;
    Int rear;
    Int size;

Public:
    Deque() {
        Front = -1;
        Rear = 0;
        Size = 0;
    }

    Bool isFull() {
        Return (size == MAX);
    }

    Bool isEmpty() {
        Return (size == 0);
    }

    Void insertFront(int element) {
        If (isFull()) {
            Std::cout << "Deque is full\n";
            Return;
        }
        If (front == -1) {
            Front = 0;
            Rear = 0;
        } else if (front == 0) {
            Front = MAX - 1;
        } else {
            Front--;
        }
        Arr[front] = element;
        Size++;
    }

    Void insertRear(int element) {
        If (isFull()) {
            Std::cout << "Deque is full\n";
            Return;
        }
        If (front == -1) {
            Front = 0;
            Rear = 0;
        } else if (rear == MAX - 1) {
            Rear = 0;
        } else {
            Rear++;
        }
        Arr[rear] = element;
        Size++;
    }

    Void deleteFront() {
        If (isEmpty()) {
            Std::cout << "Deque is empty\n";
            Return;
        }
        If (front == rear) {
            Front = -1;
            Rear = -1;
        } else if (front == MAX - 1) {
            Front = 0;
        } else {
            Front++;
        }
        Size--;
    }

    Void deleteRear() {
        If (isEmpty()) {
            Std::cout << "Deque is empty\n";
            Return;
        }
        If (front == rear) {
            Front = -1;
            Rear = -1;
        } else if (rear == 0) {
            Rear = MAX - 1;
        } else {
            Rear--;
        }
        Size--;
    }

    Int getFront() {
        If (isEmpty()) {
            Std::cout << "Deque is empty\n";
            Return -1;
        }
        Return arr[front];
    }

    Int getRear() {
        If (isEmpty()) {
            Std::cout << "Deque is empty\n";
            Return -1;
        }
        Return arr[rear];
    }
};

Int main() {
    Deque dq;
    Dq.insertRear(5);
    Dq.insertRear(10);
    Std::cout << "Rear element: " << dq.getRear() << std::endl;
    Dq.deleteRear();
    Dq.insertFront(15);
    Std::cout << "Front element: " << dq.getFront() << std::endl;
    Dq.deleteFront();
    Return 0;
}


