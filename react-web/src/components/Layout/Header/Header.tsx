import { useEffect, useState } from "react";
import "./Header.css";
import { MessagingObservable } from "../../../services/notifications.service";
import { NavItem } from "./NavItem/NavItem";
import { MessageInterface } from "../../../models/notification.model";
import { Alerts } from "../Alerts/Alerts";
import { delay } from "rxjs";
import ButtonNav from "../Buttons/ButtonNav/ButtonNav";
import BlockColorPrimary from "../Buttons/BlockColorPrimary/BlockColorPrimary";
import { useNavigate} from "react-router-dom";

const navItems = [
  { to: "/me", icon: "📋", name: "home" },
  { to: "/add-gift", icon: "🎁", name: "about" },
  { to: "/add-funds", icon: "💰", name: "contact" },
  { to: "/messages", icon: "🔔", name: "messages" },
];

export const Header = () => {
 
  const navigate = useNavigate();
  const [totalNumeberOfNotifications, setTotalNumberOfNotifications] = useState<number>(0);

  const handleNavClick = (navItem: string) => {
    navigate(navItems.find(item => item.name === navItem)?.to || "/");
  };
  
  // const source = interval(5000);
  useEffect(() => {
    const unsubscribe = MessagingObservable.onMessageReceived()
      .pipe(delay(2000))
      .subscribe((message: MessageInterface) => {
        console.log("Message received", message);
        setTotalNumberOfNotifications((prev) => prev + 1);
      });

    return () => {
      unsubscribe.unsubscribe();
    };
  }, []);

  return (
    <section className="header-container">
      <header className="header">
        <nav className="nav">
          <ul className="nav-list">
            {navItems.map((item) => (
              <NavItem
                key={item.name}
                to={item.to}
              >
                <BlockColorPrimary>

                  <ButtonNav
                    label={item.name}
                    icon={item.icon}
                    name={item.name}
                    handleNavClick={handleNavClick}
                    totalNumeberOfNotifications={totalNumeberOfNotifications}
                  />
                </BlockColorPrimary>
              </NavItem>
            ))}
          </ul>
        </nav>
      </header>
      <Alerts />
    </section>
  );
};
