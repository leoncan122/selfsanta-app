export interface useWebsocket {
    connect: () => void;
    disconnect: () => void;
    sendMessage: (message: Message) => void;
    onMessage: (callback: (message: Message) => void) => void;
    isConnected: boolean;
}
import { useState, useEffect } from 'react';
import { messagingService } from '../services/messaging.service';
import { Message } from '../mocks/messages';



export function useWebsocket  (url: string): useWebsocket  {   
    const [isConnected, setIsConnected] = useState<boolean>(false);

    const connect = () => {
        messagingService.connect(url);
        setIsConnected(true);
    };

    const disconnect = () => {
        if (messagingService.socket) {
            messagingService.socket.close();
            setIsConnected(false);
        }
    };

    const sendMessage = (message: Message) => {
        console.log("Sending message:", typeof message);
        messagingService.sendMessage(message);
    };

    const onMessage = (callback: (message: Message) => void) => {
        messagingService.onMessage(callback);
    };

    useEffect(() => {
        return () => {
            disconnect();
        };
    }, [url]);

    return { connect, disconnect, sendMessage, onMessage, isConnected };
}