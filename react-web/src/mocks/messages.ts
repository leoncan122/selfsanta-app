
export interface Message {
    id: string;
    from: string;
    to: string;
    body: string;
    timestamp: Date;
    thread_id: string;
    isRead?: boolean; // Optional property to indicate if the message has been read
}

export const MESSAGES_LIST: Message[] = [
    {
        id: "msg3213-john-s-jane",
        from: "john@example.com",
        to: "jane@example.com",
        body: "Don't forget about our meeting tomorrow at 10 AM.",
        timestamp: new Date(),
        thread_id: "thread1",
        isRead: false, // Example of a message that has not been read
    },
    {
        id: "msg3213-jane-s-john",
        from: "jane@example.com",
        to: "john@example.com",
        body: "Got it, see you then!",
        timestamp: new Date(),
        thread_id: "thread1",
        isRead: false, // Example of a message that has not been read
    },
    {
        id: "msg3213-alice-s-bob",
        from: "alice@example.com",
        to: "bob@example.com",
        body: "The project is on track for completion next week.",
        timestamp: new Date(),
        thread_id: "thread2",
        isRead: false, // Example of a message that has not been read
    },
    {
        id: "msg3213-bob-s-alice",
        from: "bob@example.com",
        to: "alice@example.com",
        body: "Great news, thanks for the update!",
        timestamp: new Date(),
        thread_id: "thread2",
        isRead: false, // Example of a message that has not been read
    },
    {
        id: "msg3213-charlie-s-dave",
        from: "charlie@example.com",
        to: "dave@example.com",
        body: "Are you free for lunch tomorrow?",
        timestamp: new Date(),
        thread_id: "thread3",
        isRead: false, // Example of a message that has not been read
    },
    {
        id: "msg3213-dave-s-charlie",
        from: "dave@example.com",
        to: "charlie@example.com",
        body: "Yes, let's meet at 12 PM.",
        timestamp: new Date(),
        thread_id: "thread3",
        isRead: false, // Example of a message that has not been read
    },
    {
        id: "msg3213-erin-s-frank",
        from: "erin@example.com",
        to: "frank@example.com",
        body: "Can you review my latest code changes?",
        timestamp: new Date(),
        thread_id: "thread4",
        isRead: false, // Example of a message that has not been read
    },
    {
        id: "msg3213-frank-s-erin",
        from: "frank@example.com",
        to: "erin@example.com",
        body: "Sure, I'll take a look this afternoon.",
        timestamp: new Date(),
        thread_id: "thread4",
        isRead: false, // Example of a message that has not been read
    },
    {
        id: "msg3213-grace-s-henry",
        from: "grace@example.com",
        to: "henry@example.com",
        body: "I'd like to request vacation time from Dec 20 to Jan 2.",
        timestamp: new Date(),
        thread_id: "thread5",
        isRead: false, // Example of a message that has not been read
    },
    {
        id: "msg3213-henry-s-grace",
        from: "henry@example.com",
        to: "grace@example.com",
        body: "Your vacation request has been approved.",
        timestamp: new Date(),
        thread_id: "thread5",
        isRead: false, // Example of a message that has not been read
    },
];

export interface Thread {
    id: string;
    lastMessage: string;
    from?: string; // Optional property to indicate the last sender
    timestamp: Date;
    // Optionally, you can add more properties like participants, unreadCount, etc.
}

export const THREADS_LIST: Thread[] = [
    {
        id: "thread1",
        lastMessage: "Got it, see you then!",
        from: "user2",
        timestamp: new Date(),
    },
    {
        id: "thread2",
        lastMessage: "Great news, thanks for the update!",
        from: "user2",
        timestamp: new Date(),
    },
    {
        id: "thread3",
        lastMessage: "Yes, let's meet at 12 PM.",
        from: "user2",
        timestamp: new Date(),
    },
    {
        id: "thread4",
        lastMessage: "Sure, I'll take a look this afternoon.",
        from: "user2",
        timestamp: new Date(),
    },
    {
        id: "thread5",
        lastMessage: "Your vacation request has been approved.",
        from: "user2",
        timestamp: new Date(),
    },
];