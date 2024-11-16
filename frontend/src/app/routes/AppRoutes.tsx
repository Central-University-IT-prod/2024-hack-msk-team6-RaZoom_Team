import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import { HomePage } from "../../pages/home/ui/Home";
import { useContext } from "react";
import { UserContext } from "../providers/user";
import AuthPage from "../../pages/auth/ui/AuthPage";
import NotFoundPage from "../../pages/notfound/ui/NotFoundPage";

const AppRoutes = () => {
    const { user } = useContext(UserContext); // Get user context

    return (
        <BrowserRouter future={{ v7_startTransition: true, v7_relativeSplatPath: true }}>
            <Routes>
                <Route path="/auth" element={user ? <Navigate to="/" /> : <AuthPage/>} />
                <Route path="/" element={user ? <HomePage /> : <Navigate to="/auth" />} />
                <Route path="*" element={<NotFoundPage/> }/>
            </Routes>
        </BrowserRouter>
    );
};

export default AppRoutes;