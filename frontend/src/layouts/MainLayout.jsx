import {Outlet} from "react-router-dom";
import Header from "../components/Header.jsx";

const MainLayout = ({ children }) => {
    return (
        <div className="flex flex-col h-[1080px] bg-[#F2E5CC] relative p-[80px] pe-[0px]">
            <div className="w-full h-[1080px] bg-[url('/background.png')] bg-center bg-no-repeat opacity-40 absolute top-0 left-0 z-1"></div>
            <Header className="z-2" />
            <main className="flex flex-1 z-2">
                {children || <Outlet />}
            </main>
        </div>
    )
}
export default MainLayout