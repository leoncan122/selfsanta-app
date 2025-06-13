import { Message } from "../../../mocks/messages";
import { Suspense, useEffect, useRef, useState } from "react";
import { useWebsocket } from "../../../hooks/useWebsocket";
import  "./MessagesChat.css";
export interface MessagesChatProps {
    threadId: string;
    // messages: Message[];
}

export const MessagesChat = ({ threadId }: MessagesChatProps) => {
    const { connect, onMessage, disconnect, sendMessage } = useWebsocket("ws://localhost:8000/ws/messages/");

    const newMessageRef = useRef<string>("");
    const [ messages, setMessages ] = useState<Message[]>([]); 
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);
    // const [connection, setConnection] = useState<WebSocket | null>(null);
    // const [connected, setConnected] = useState<boolean>(false);
    const connecToSocket = async (): Promise<void> => {
        try {

            setLoading(false);

            connect();
            onMessage((msg: Message) => {
                setMessages((prev) => [...prev, msg]);
            });
        } catch (error) {
            console.error("Failed to connect to messaging service:", error);
            setError("Failed to connect to messaging service");
            setLoading(false);
        }
    }

    useEffect(() => {
        setLoading(true);
        setError(null);
        connecToSocket()
        return () => {
            disconnect();
        };
    }, [threadId]);


    if (loading) {
        return <div>Loading...</div>;
    }
    if (error) {
        return <div>Error: {error}</div>;
    }
   
    const handleSendMessage = () => {
        const messageToSend: Message = {
            id: Date.now().toString(),
            from: "User",
            to: "Recipient",
            thread_id: threadId,
            body: newMessageRef.current,
            timestamp: new Date(),
        };
        // Here you would send the message to the server
        // For now, we just add it to the local state
        // setMessages((prev) => [...prev, messageToSend]);
        sendMessage(messageToSend);
    }
    
    return (
        <div className="messages-chat">
            <h2>Chat Messages</h2>
            <Suspense fallback={<div>Loading messages...</div>}>
                {/* Here you would map through the messages for the specific thread */}
                {messages.map(({ from, body}, index) => (
                    <div key={index} className="message-item">
                        <div className="message-details">
                            <p className="message-from">{from}</p>
                            <p className="message-body">{body}</p>
                        </div>
                        <div className="message-info">
                            {/* <span className="message-timestamp">{timestamp}</span> */}
                        </div>
                    </div>
                ))}
            </Suspense>
            <div className="message-input-container">
                <textarea
                name="message-input"
                placeholder="Type your message here..."
                className="message-input"
                onChange={(e) => newMessageRef.current = e.target.value}
                    />
                <button onClick={handleSendMessage} className="send-message-button">
                    Send 
                </button>
            </div>
            
        </div>
    );
}