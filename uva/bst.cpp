#include <stdio.h>
#include <vector>
using namespace std;

typedef struct Node {
  int val;
  struct Node* left;
  struct Node* right; 
  struct Node* parent;
  Node(int num, struct Node* leftChild, struct Node* rightChild, struct Node* nodeParent) {
    val = num;
    left = leftChild;
    right = rightChild;
    parent = nodeParent;
  }
} Node;

void postorder(Node* root) {
  vector<Node*> m;
  if (!root) {
    return;
  }
  Node* cur = root;
  while (1) {
    while (cur) {
      if (cur->right) {
        m.push_back(cur->right);
      }
      m.push_back(cur);
      cur = cur->left;
    } 
    cur = m.back();
    m.pop_back();
    if (!m.empty() && m.back() == cur->right) {
      m.pop_back();
      m.push_back(cur);
      cur = cur->right;
    }
    else {
      printf("%d\n", cur->val);
      cur = 0;
    }
    if (m.empty()) {
      break;
    }
  }
}

void inorder(Node* root) {
  if (root->left) {
    inorder(root->left);
  }
  printf("%d\n", root->val);
  if (root->right) {
    inorder(root->right);
  }
}

int main() {
  vector<Node*> m;
  int a;
  if (scanf("%d", &a) != 1) {
    return 0;
  }
  Node* root = new Node(a, 0, 0, 0);
  m.push_back(root);
  Node* node;
  while(scanf("%d", &a) == 1) {
    node = new Node(a, 0, 0, 0);
    if (m.back()->val >= node->val) {
      m.back()->left = node;
      node->parent = m.back();
      m.push_back(node);
      continue;
    }
    Node* top;
    while (m.back()->val < node->val) {
      top = m.back();
      m.pop_back();
      if (m.empty()) {
        break;
      }
    }
    top->right = node;
    node->parent = top;
    m.push_back(node);
  }
  postorder(root);
  return 0;
}
