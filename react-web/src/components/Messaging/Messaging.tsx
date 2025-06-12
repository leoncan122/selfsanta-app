import PageViewWrapper from "../Layout/PageViewWrapper/PageViewWrapper";
import './Messaging.css';
import { ThreadsList } from "./ThreadsList/ThreadsList";
import { THREADS_LIST } from "../../mocks/messages";
import { MessagesChat } from "./MessagesChat/MessagesChat";


export const MessagingPanel = () => {
    

    
    
    return (
        <PageViewWrapper>
            
            <div id="messaging-panel-header">
                <h2>
                    Messages
                </h2>
                
            </div>
            {/* <button onClick={handleNotification}>Send Message</button> */}
            <ul className="primary-list">
            <section className="chat-container">
                <ThreadsList thread={THREADS_LIST} />
                <MessagesChat threadId={THREADS_LIST[0].id} />
            </section>
            
        </ul>
        </PageViewWrapper>
    )
}