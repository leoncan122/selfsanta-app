import PageViewWrapper from "../../Layout/PageViewWrapper/PageViewWrapper";
import { Link } from "react-router-dom";
import { Thread } from "../../../mocks/messages";
import './ThreadsList.css';

export interface ThreadsListProps {
    thread: Thread[];
}

export const ThreadsList = ({ thread }: ThreadsListProps) => {
    if (thread.length === 0) {
        return (
            <PageViewWrapper>
                <h2>Messaging Panel</h2>
                <p>No messages found</p>
            </PageViewWrapper>
        )
    }


    return (
        <div>
            <ul className="threads-list">
                {thread.map(({ id, from,lastMessage, timestamp }) => (
                    <Link to={`/messages/${id}`} key={id}>
                        <li key={id} className="thread-item">
                            <h6 className="thread-title">{from}</h6>
                            <div className="thread-details">
                                <p className="thread-body">{lastMessage}</p>
                            </div>
                            <div className="thread-info">
                                <span className="message-timestamp">{timestamp.toLocaleString()}</span>
                            </div>
                        </li>
                    </Link>
                ))}
            </ul>
        </div>
    );
}