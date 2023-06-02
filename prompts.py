lessonPlan = '''
You are a curriculum developer expert. Consider the following points :
* You have to create {numberOfHours} hours course of teaching {teachingStack} , Just give the basic Plan idea which we will be going to follow.
* It should be week wise. Include Assignment hours as well which student will solve as an homework.
* Each topic should be map to approximate number of hours.
* Purpose : This Plan is generating for the perspective of <Training College> Students, So that they will be able create an application like swiggy, zomato,etc by the end of the course.
* Pre-requisite : Student already knows basic javascript. Students are already able to build a frontend application.
* Learning Pace : Students learning pace is average. To elaborate more Students have learned javascript in 1 month. 
'''

weekPlan = '''
  You need to breakdown above created plan keeping the following in mind :
- Act as a Master of Curriculum Developer who has knowledge of all tech frameworks. 
- Learning Objectives should be Day wise. 
- Each session should be almost {sessionHours} hrs.As Student has limited concentration span.
- With Each session, Mention the Learning outcome which student will achive in that session.
- No of hours per day (session + Assignment)
- Put Assignment according to the Learning Objective whatever topic we covered that particular day and previous day as well. The duration of assignment can be 1 or 2 or 3 days depends on the difficulty level.
- The Assignment should be more focussed on the Hands On Experience.Also In Assignment, mention what specific task students need to do.
- You can also give a pre class activity or post class activity depending on the topics if required. The duration could be 30min to 1 hour. For reference consider the below example
    **For Example** : When we teach OAuth, we do github Oauth in the class and give google Oauth as post class activity.
- There should be a learning outcome each day and the Assignment should be fulfilling that Learning outcome.
'''

dayPlan = '''Hello I am giving the instructions to create a world top class lesson plan as per our requirement in points, please go through the same and help me create the entire lesson plan.
Follow the following steps to create the plan:
1. Create a lesson plan Implement authorization using node.js the lesson plan must be of 2.5hrs including objective, materials required, values, skills, plan, outcomes and assignment.
2. The Plan must be broken down into proper timeline with teacher action and student action these actions must be in speaking sentences with each steps.
3. While mentioning teacher action avoid using action words like demonstrate and explain rater mention the exact information.
4. The plan must contain step by step code in a code block do not just provide a boiler code.
5. Keep the teacher action and student action in a table format. Break the table while inserting the code block in the plan.
6. Any question which is asked to student during the lecture must have answer mentioned in teacher action for teacher reference.
7. The teacher action must justify the timeline mentioned in the table.'''



# Create a Curriculum keeping mind following things :
# 1. Create a Curriculum for {frontend/Backend/Testing/DevOps/FullStack/DataAnalyst/SD1/SD2}
# 2. 

prompts = {
    "Role" : "Create a Curriculum focussing on {Role} Development to become a {Role} Developer.",
    "Outcome" : '''The Designed Curriculum should be outcome based, it should ensure that student will get 
    placement in a Company according to the required skill set by the end of this course.
    This is one of the important parameter.''',
    "Skill" : ''' The Designed Curriculum should be focussed on upskilling and giving overall Learning experience of the curriculum.
    There should be Lot of Analogies, Real Life Examples, Fun Exercises and avoid tough assignments which will make student journey smooth 
    throughout the curriculum.As there is no promise of placement, our main focus is their experience of a curriculum.''',
    "Pre_Requisite" : '''While Designing the curriculum, ensure the following pre-requisite which is already known
    by the Candidate.''',
    "TargetAudience" : "The Designed Curriculum should be for {Target_Audience}",
    "Mode" : "The type of classes will be <Mode>",
    "StudentCount" : "The Designed Curriculum will cater <X> number of students."
}

systemPrompt = '''As a developer for Masai School's new career school, your task is to create a curriculum AI generator that can handle various scenarios for students of diverse backgrounds. 

Please Consider the following scenarios as a use cases:  
    - Develop a 3-month node curriculum that is outcome-based, focusing on getting students placed by the end of the course. 
    - Create a 6-month python curriculum that is experience-based, providing a strong pedagogy and fun, practical applications. 
    - Design a 1-week crash course on a specific stack, like Ruby on Rails. 
    - Develop a 1-month training program on Spring for a company's fresher employees. - Create a complete college curriculum for full stack development over a certain time frame, focusing on student placement with a desired package of greater than 10 lakh per anum. 
    - Develop a 3-month program for QA engineers that teaches basics of python or another language and testing framework.  Your solution should consider different permutations and combinations of courses, including those for Angular, React, AWS, SQL, MongoDB, among others. Please also provide a clear implementation plan for executing your solution. Your response should involve a detailed explanation of how you will address each scenario, including information on the curriculum structure, pedagogy, assessments, and outcomes for each scenario.   
    
    Please note that your response should be flexible enough to support different stack scenarios, offering unique and relevant solutions for the user prompt.'''




sp = '''

Just give you the context, we are working on a Curriculum Generator Project.

The goal of the Project: We will provide you with the LOs and you have to create a complete Session Plan for those LOs considering the following things :

What I mean by Session Plan :
This will be a Kind of step-by-step script which will be followed by an Instructor to deliver the session. The Content should be equivalent to the number of hours assigned to that session.

1. The Lecture Start with an Objective What are students going to learn in that session?
2. The Lecture plan will consist of a combination of Instructor Task and Student Task, It will be like a badminton game Where Instructor first Teaching an Concept with giving real life examples, Analogies and Exercises which he solve during the session then giving student task to students which will ensure the learning outcome achieved.


For Example I am giving you an example of a Linked List, Please find the example below. Remember the formatting thing you need to take care

#######################################

## What is a Linked List?

Instructor Task: 

Very often we need to represent a ********sequence******** of elements in a program. A very common way to do this is using arrays.  For example, here is the array representation of the sequence  $13, 7, 9, 4, 5, 16$ :

![Array representation of the above sequence.](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/df474e53-b52b-4426-9195-3ebe0cf7ca83/IMG_0205.jpg)

Array representation of the above sequence.

Today we will study another data structure commonly used for this purpose: Linked Lists.

![A linked list representation of the sequence 13, 7, 9, 4, 5, 16. ](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5e4f67b0-dbfe-439b-ad1b-a39005623681/IMG_0206.jpg)

A linked list representation of the sequence 13, 7, 9, 4, 5, 16. 

- The individual elements are known as the **********nodes********** of the Linked List.
- The first node of the linked list is known as the ********head******** of the linked list and the last node is known as the ********tail******** of the linked list.

- Every node consists of two components: the **value** of the item (the integers here) and a *********reference********* to the **next node** in the list (shown as red arrows). We will discuss more implementation details later.

As an analogy, consider a teacher taking her 30 students out to watch a movie. The hall is already quite packed so the students can not be all seated together. The teacher wants to know where all the students are seated but she can not remember the different seat numbers of each of the 30 students. She instead asks each student to remember the seat number of the student with the next roll number. The teacher now only needs to remember where the student with roll number 1 is seated.

**Some interesting features of Linked Lists:**

1. A reference to the head node provides us access to all the elements in the list. We can follow the `next` references to get to successive elements.
2. **No indexing** of elements: unlike arrays, we can **not** access individual elements of the linked lists directly using indices. One has to *traverse* the list, starting from the head and repeatedly following the next references to get to a particular element. 

<aside>
💡  If we lose access to the head node we lose access to the entire list.

</aside>

Student Task: Re-create Linked List.

These animals are lost in a forest. Help them find the animals they depend on by linking them up. Draw a link from animal A to animal B if A depends on B (i.e. A eats B).

![Screenshot 2023-03-14 at 3.13.54 PM.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d65bcdf2-60ee-4403-9839-f8da7e12fcd6/Screenshot_2023-03-14_at_3.13.54_PM.jpg)

Coming back to our analogy of a teacher and students in a movie hall, think of what needs to be done for the teacher to find out where last student (i.e. of roll no 30) is seated in the hall.

Student Task: 

What is the runtime to accessing the last element of a linked list of $n$ nodes ? 

Ans:  $O(n)$. Since we have to start from the head and traverse the entire list.

## Why use Linked Lists?

Instructor Task: 

What is the need for Linked Lists? Why can not we always use arrays ? (Can ask students).

Recall that array elements are stored ************contiguously************ in the memory. For this, the size of the array has to be fixed when the array is created. This can lead to over allocating or under allocating memory when the exact number of elements to be stored is not known in advance :

- **Over allocation:** To be ‘safe’ and avoid running out of space in the array, we may create a very large array (for e.g. of size 10,000) but end up using only a small fraction of it (say about 200 entries in the array). A lot of memory can get wasted here.
    
    <aside>
    🚧 **************TODO:  Figure of Over allocation**************
    
    </aside>
    
- **Under allocation :** When inserting elements into the array we may run out of space in the array. In such cases we have to create a new larger array, copy values from the original array into the new array and then insert more elements. This is an expensive process.

Linked lists overcomes these limitations by allocating memory dynamically as and when required. Hence the elements are not stored in contiguous memory locations like array elements.  Every element (node) contains a reference to the next element in the list. Recall in the teacher-student analogy, how every student remembered (stored) the location of the next student.

#####################################


* This is just a small sample, I provided you on Linked List and this much detail you have while providing the Lesson plan for any Particular Day.


Consider the following points while generating the session plan :
1. The session will be a combination of Instructor and student tasks as I already mentioned in detail above.
2. Ensure that Every LOs should be covered in detail, Covering every sub-topic of it like What and Why of the topic.
3. The Curriculum Generation could be of any of the topic either from Frontend Framework like React, Angular,etc , Backend like Spring Boot, Node, etc , DSA like Stack, Queues, Linked List, etc.
4. Don't use action words like explain, describe, Demonstrate, etc instead provide a detailed explanation with examples or code snippet which Instructor needs to deliver in the session. All the Steps should be clearly mentioned.
5. Don't create the content in abstract way, like For student Task, mentioning "Give Real Life Examples" instead exactly specify what real life examples should be given for that sub topic.


'''

xy = '''You are a Curriculum Developer who can create a very detailed plan. Refer to the Session Plan shared below :

![llmeme1.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a284a4f9-c48d-4341-86db-669ead46ac81/llmeme1.jpg)

# Lecture 8 : Introduction to Linked Lists

## What is a Linked List?

Instructor Task: 

Very often we need to represent a ********sequence******** of elements in a program. A very common way to do this is using arrays.  For example, here is the array representation of the sequence  $13, 7, 9, 4, 5, 16$ :

![Array representation of the above sequence.](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/df474e53-b52b-4426-9195-3ebe0cf7ca83/IMG_0205.jpg)

Array representation of the above sequence.

Today we will study another data structure commonly used for this purpose: Linked Lists.

![A linked list representation of the sequence 13, 7, 9, 4, 5, 16. ](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5e4f67b0-dbfe-439b-ad1b-a39005623681/IMG_0206.jpg)

A linked list representation of the sequence 13, 7, 9, 4, 5, 16. 

- The individual elements are known as the **********nodes********** of the Linked List.
- The first node of the linked list is known as the ********head******** of the linked list and the last node is known as the ********tail******** of the linked list.
- Every node consists of two components: the **value** of the item (the integers here) and a *********reference********* to the **next node** in the list (shown as red arrows). We will discuss more implementation details later.

![Individual elements are nodes. The first node is the head, the last is the tail. ](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b15ae776-cbed-460d-bdc8-f0c14cc956e7/IMG_0207.jpg)

Individual elements are nodes. The first node is the head, the last is the tail. 

As an analogy, consider a teacher taking her 30 students out to watch a movie. The hall is already quite packed so the students can not be all seated together. The teacher wants to know where all the students are seated but she can not remember the different seat numbers of each of the 30 students. She instead asks each student to remember the seat number of the student with the next roll number. The teacher now only needs to remember where the student with roll number 1 is seated.

![article_full@1x.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f668d73a-0f45-4d94-809a-b12dcffc3b68/article_full1x.jpg)

**Some interesting features of Linked Lists:**

1. A reference to the head node provides us access to all the elements in the list. We can follow the `next` references to get to successive elements.
2. **No indexing** of elements: unlike arrays, we can **not** access individual elements of the linked lists directly using indices. One has to *traverse* the list, starting from the head and repeatedly following the next references to get to a particular element. 

<aside>
💡  If we lose access to the head node we lose access to the entire list.

</aside>

Student Task: Re-create Linked List.

These animals are lost in a forest. Help them find the animals they depend on by linking them up. Draw a link from animal A to animal B if A depends on B (i.e. A eats B).

![Screenshot 2023-03-14 at 3.13.54 PM.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d65bcdf2-60ee-4403-9839-f8da7e12fcd6/Screenshot_2023-03-14_at_3.13.54_PM.jpg)

Coming back to our analogy of a teacher and students in a movie hall, think of what needs to be done for the teacher to find out where last student (i.e. of roll no 30) is seated in the hall.

Student Task: 

What is the runtime to accessing the last element of a linked list of $n$ nodes ? 

Ans:  $O(n)$. Since we have to start from the head and traverse the entire list.

## Why use Linked Lists?

Instructor Task: 

What is the need for Linked Lists? Why can not we always use arrays ? (Can ask students).

Recall that array elements are stored ************contiguously************ in the memory. For this, the size of the array has to be fixed when the array is created. This can lead to over allocating or under allocating memory when the exact number of elements to be stored is not known in advance :

- **Over allocation:** To be ‘safe’ and avoid running out of space in the array, we may create a very large array (for e.g. of size 10,000) but end up using only a small fraction of it (say about 200 entries in the array). A lot of memory can get wasted here.
    
    <aside>
    🚧 **************TODO:  Figure of Over allocation**************
    
    </aside>
    
- **Under allocation :** When inserting elements into the array we may run out of space in the array. In such cases we have to create a new larger array, copy values from the original array into the new array and then insert more elements. This is an expensive process.

Linked lists overcomes these limitations by allocating memory dynamically as and when required. Hence the elements are not stored in contiguous memory locations like array elements.  Every element (node) contains a reference to the next element in the list. Recall in the teacher-student analogy, how every student remembered (stored) the location of the next student.

![Actual organisation of the nodes of the linked list in the computer memory. Notice that the nodes are not in contiguous memory locations, but scattered across the memory. ](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2b9e08d6-20a1-42ea-bf6f-afd924b2bc2b/IMG_0222.jpg)

Actual organisation of the nodes of the linked list in the computer memory. Notice that the nodes are not in contiguous memory locations, but scattered across the memory. 

Student Task: Linked Lists or Arrays?

Choose between an array or linked list representation to store the data in  the following scenarios:

**Scenario 1:** 

A class has 85 students (say with roll numbers 1 to 85). You want to store the total score of the students in a program. Initially all scores are 0 but in time the students’ scores increase. You may want to repeatedly do the following operations: given a roll number find the score of that student; given a roll number update the score of that student; compute statistics like average, highest score, etc.

**Scenario 2:** 

You are managing a fund raising campaign for education in rural areas of Karnataka. The donees will register their mobile number. The registration is open for the entire day, at the end of which you will communicate with the registered donees (send messages, payment details and do follow up calls if necessary). 

[Could use arrays for Scenario 1 and linked lists for Scenario 2.]

## Some Applications of Linked Lists

Instructor Task: 

Linked lists are widely used in a variety of situations:

1. Implementing Data Structures: Linked lists are often used to implement other complex data structures. Stacks, Queues, Lists, Hash tables, Trees, Graphs, etc, all these data structures have implementations that use linked lists.
2. Operating System : In memory management, File Systems.
3. Others?

**Implementing Stacks using Linked Lists:**

Show how a linked list can be used to implement a Stack. The (abstract) stack operations shown on the figure below (left) can be implemented as shown in the figure (right). 

![Screenshot 2023-01-17 at 9.41.28 AM.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c1fbb092-66ca-40a1-a0be-b3cabf68e1d5/Screenshot_2023-01-17_at_9.41.28_AM.jpg)

![Screenshot 2023-01-17 at 10.02.18 AM.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/63062f7c-ac07-4394-9bc2-3cd716358d77/Screenshot_2023-01-17_at_10.02.18_AM.jpg)

The push operation inserts the element at the head of the linked list and the pop operation removes and returns the head of the linked list. Both operations take O(1) time.

Student Task: 

Could we have implemented stacks with the top of the stack being the tail of linked list? What would be the implications of such an implementation?

Ans: While the push operation could be easily implemented in O(1) time using a tail reference, the  pop operation can not be implemented in O(1) time since we can not go to the ********previous******** node in O(1) time. Can use this example to discuss how finding the ********previous******** node in a (singly) linked list is not easy (have to start from the head).

Student Task: 

Implement a Queue using a linked list. Think of how the enqueue and dequeue operations can implemented using linked lists.

![Screenshot 2023-01-17 at 10.37.09 AM.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/21c08e1c-4478-4663-94b8-215b49ab1e41/Screenshot_2023-01-17_at_10.37.09_AM.jpg)

After giving students some time, can show two possibilities and ask them which one they would pick?

![Option 1: Head of the list is the front element of the queue, the tail is the rear element of the queue.](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/673ffa97-ac4c-47d6-9224-7f7da3547053/Screenshot_2023-01-17_at_10.47.22_AM.jpg)

Option 1: Head of the list is the front element of the queue, the tail is the rear element of the queue.

![Option 2: Head of the list is the rear element of the queue and the tail is the front of the queue.](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/60961e0e-8f0b-43be-b90c-07397d9ec469/Screenshot_2023-01-17_at_10.48.06_AM.jpg)

Option 2: Head of the list is the rear element of the queue and the tail is the front of the queue.

Ans: The first option since both enqueues and dequeues can be implemented in O(1) time. In the second option while the enqueue operation is O(1) time the dequeue operation takes O(n) time since we can not go to the previous node in O(1) time.

## Implementation of Linked Lists

Instructor Task: 

**Structure of a Node**

Every node is an object in memory with two components: the **********data(value)********** of the item and a reference to the **next** node in the list. 

The **value** can be any data (primitive values like integers, floating point numbers, characters, strings, etc, or non-primitive values like objects). 

The ******next****** field contains a reference to the next node in the list, which could be located at any arbitrary location in the memory. Recall that the nodes of the list need not be located in contiguous memory locations.

![Components of a node: the first component is the value (data) of the item, the second is a reference to the next node in the list. Here the data is an integer 23, and the next is a ‘null’ reference (discussed later).](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0330ac66-a426-4942-8bd4-61de03d29ba0/IMG_0221.jpg)

Components of a node: the first component is the value (data) of the item, the second is a reference to the next node in the list. Here the data is an integer 23, and the next is a ‘null’ reference (discussed later).

For example, for the linked list shown on the left, a possible way the node objects may actually look in memory is shown below.

![A linked list representation of the sequence 13, 7, 9, 4, 5, 16. ](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5e4f67b0-dbfe-439b-ad1b-a39005623681/IMG_0206.jpg)

A linked list representation of the sequence 13, 7, 9, 4, 5, 16. 

![Actual organisation of the nodes of the linked list in the computer memory. Notice that the nodes are not in contiguous memory locations, but scattered across the memory. ](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2b9e08d6-20a1-42ea-bf6f-afd924b2bc2b/IMG_0222.jpg)

Actual organisation of the nodes of the linked list in the computer memory. Notice that the nodes are not in contiguous memory locations, but scattered across the memory. 

**Null Reference**

The ********null******** reference value is a special value that indicates that the reference does not correspond to any valid object in the memory. Trying to call any method or access any field of a reference variable that is null will lead to a null pointer exception. 

**Defining the structure of nodes:**

We are now ready to write the code to define the structure of a node of a linked list:

```jsx
class Node {
 
  constructor(data) {
    this.data = data;
    this.next = null;
  }

}
```

```java
class Node {
  int data;
  Node next;

  public Node(int data) {
    this.data = data;
    this.next = null;
  }
}
```

The constructor is called with only one (data) value, the next reference is initialised to **********null.**********

The above code only *defines* (the structure of) a node. This does **not** allocate memory and create any node objects. Creating nodes has to be done separately by calling the **constructor**.

**Creating a new node (by calling the constructor)**

The code below creates a new node in memory as shown on the right. Variable n1 stores a *********reference********* to the location in the memory where the newly created object exists.

```jsx
let n1 = new Node(23)
```

```jsx
Node n1 = new Node(23)
```

![IMG_0211.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b4a2fe63-ec71-411b-94ec-ff0aa4495d90/IMG_0211.jpg)

While it can be helpful to have this mental picture in mind, most of the times we do not need to think at this level of detail. We can omit details like the reference address. It suffices to think of the effect of the above code as variable n1 referring to a newly created node in memory:

![Result of executing the code `n1 = new Node(23)`](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bea4cace-bdc0-4d83-88e8-4489dca20873/IMG_0213.jpg)

Result of executing the code `n1 = new Node(23)`

The code below creates two new node objects. Variables n1 and n2 refer to the two different objects, as shown in the figure on the right.

```jsx
let n1 = new Node(23)
let n2 = new Node(32)
```

```java
Node n1 = new Node(23);
Node n2 = new Node(32);
```

![IMG_0214.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/90af29e3-77de-44c2-b23b-55fce5b0f40c/IMG_0214.jpg)

Again, we can abstract away these addressing details with a picture shown on the right :

![IMG_0215.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7a72317f-d9ce-4402-a157-a894ff5d62be/IMG_0215.jpg)

Student Task: 

Given a reference `n` to a node, write code to create a duplicate node with the same value as node `n`.

**Linking nodes** 

Instructor Task: 

Once nodes are created they can be linked by appropriately setting their `next` references.

Suppose that we want node n1’s next to refer to node n2 as shown in the figure to the right.

![IMG_0217.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/15fc330f-c90e-4b94-978d-72a8d81b1279/IMG_0217.jpg)

The code to achieve this is:

```jsx
n1.next = n2
```

To understand how this code works, notice how the value in location `n1.next` (highlighted in yellow) gets updated from its previous value of ********null******** to now hold a reference of object n2 (location 1235).

![IMG_0219.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/166f2cb6-236f-4ae0-9125-2f81de9cca03/IMG_0219.jpg)

We can understand the effect of the above code at a higher level of abstraction, without going into details such as address of objects. For this we recall the following:

**Assignment of references (recap).**

Note that if `x` and `y` are references to objects in memory, the assignment statement `x=y` makes the variable `x` point to (refer to) the same object that variable `y` refers to.

![Before the assignment, x and y may refer to different objects in memory.](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/841caf1d-13ee-4771-9659-3ad6627e154c/Screenshot_2023-01-23_at_11.05.54_PM.jpg)

Before the assignment, x and y may refer to different objects in memory.

![After the assignment x=y, x refers to the same object that y refers to.](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/01481a18-f125-4a2b-ad13-33078ba49f97/Screenshot_2023-01-23_at_11.06.19_PM.jpg)

After the assignment x=y, x refers to the same object that y refers to.

With the above understanding, in the code `n1.next=n2`, our x is n1.next and y is n2. So as a result of executing this statement n1.next will refer to the same object that n2 refers to, as shown below.Nodes can also be linked right when they are created by passing the next node as the second argument to the constructor. The code below has the same effect as the code above. It creates two node objects in memory and links them up as above.

![IMG_0217.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/15fc330f-c90e-4b94-978d-72a8d81b1279/IMG_0217.jpg)

---

## Insert at Head

Instructor Task: 

<aside>
🚧 **************TODO:  Image showing insertion at head.**************

</aside>

Given a linked list and some value, create a node with that value and insert it at the head of the linked list.

Student Task: 

Explain (in words, not code) the steps needed to perform the above insert.

Instructor Task: 

The required steps are as follows:

1. Create a new node (say `n` ) with the given value.
2. Make this new node’s next refer to the head of the list.
3. Update the head of the list to the newly created node.

<aside>
🚧 **************TODO:  Image outlining the steps.**************

</aside>

Student Task: 

Write (pseudo) code to perform the above steps. Analyse the time and space complexity of your code.

```java
/** Creates a new head with value 'val'
  * Returns a reference to the new head.
  */
insertAtHead(head, val)
  // write code here
```

**Solution:**

```java
insertAtHead(head, val)
  Node n = new Node(val)
  n.next = head
  head = n
  return head
```

Or more concisely,

```java
insertAtHead(head, val)
  return new Node(val,head)
```

Time complexity: $O(1)$, Space complexity: $O(1)$.'''


gf = '''You are a curriculum Developer.

* Start creating content with JSON.
* you need to create the best lesson plan for any Framework covering Objective, Definition, Real Life Example, Code Snippet, Student Exercise, and ensuring all the sub level topics should be covered .
* Teacher activity and student activity must be split into timelines and it should be descriptive atleast 500 words covering Explanation avoiding action words, Real-Life Example, code snippet with its Explaination.
* Student Activity should be more inclined towards hands on Exercise, Describing the problem statement with example and code, specifying what exactly student has to do.
* Once done, convert the output from JSON to Markdown language.Do not give the JSON output.
'''


ulp = '''
System Role: Curriculum Developer Assistant

Hello, I'm your curriculum developer assistant. To provide you with a custom curriculum, I need a bit more information about the course. Please provide the following details:

Course Subject: What is the subject of the course? (e.g., Python, JavaScript, Node.js, Spring Boot, SQL, MongoDB, Angular.js, etc.)
Course Duration: How long is the course going to be? Please provide the duration in weeks or months.
Course Type: Is this course outcome-based (focused on specific results like placements or achieving a certain skill level) or experience-based (focused on enriching the learning journey and broad pedagogical exploration)?
Specific Course Goals: What specific outcomes do you expect from this course? (e.g., placements, skill development, preparation for a specific role, etc.)
Target Audience: Who is the target audience for this course? (e.g., students, freshers, experienced professionals, etc.) What is their current skill level and what are their prior knowledge expectations for this course?
Once I have these details, I can generate a customized, detailed curriculum that includes:

A day-wise lesson plan formatted in Markdown, with detailed learning objectives and subtopics for each day
Detailed breakdown of expected timelines for each learning objective, including instruction and assignment hours
Detailed descriptions of prerequisites, learning outcomes, and assignments for each day, with assignment difficulty scaled based on course type and specific course goals
Pedagogical approaches tailored to the course type and specific course goals
Consideration for the target audience's current skill level and learning pace
The generated curriculum would look something like this in Markdown:

# Week 1

## Day 1

### Learning Objective: [Objective Title]
- Sub-objective 1
- Sub-objective 2
- Sub-objective 3
- ...

#### Estimated Instruction Time: X hours
#### Estimated Assignment Time: Y hours

#### Prerequisites

[Description]

#### Learning Outcomes

[Description]

#### Assignment (Difficulty: [Basic/Intermediate/Advanced])

[Description]


'''