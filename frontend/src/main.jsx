import {StrictMode} from 'react'
import {createRoot} from 'react-dom/client'
import AppRoutes from "./router.jsx";
import './index.css'

createRoot(document.getElementById('root')).render(
    <StrictMode>
        <AppRoutes/>
    </StrictMode>
)
