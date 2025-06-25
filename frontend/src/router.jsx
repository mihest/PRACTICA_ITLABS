import React from "react";
import {BrowserRouter as Router, Routes, Route, Navigate} from "react-router-dom";
import HomePage from "./pages/HomePage.jsx";
import MainLayout from "./layouts/MainLayout.jsx";

const AppRoutes = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={
                    <MainLayout>
                        <HomePage />
                    </MainLayout>
                } />

                <Route path="*" element={<Navigate to="/" replace/>} />
            </Routes>
        </Router>
    )
}

export default AppRoutes;