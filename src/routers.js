import React from "react";
import { createBrowserRouter } from "react-router-dom";
import Home from './pages/Home';
import Users from './pages/Users';
import About from './pages/About';
import Story from './pages/Story';
import Root from './pages/Root';



const router = createBrowserRouter([
    {
        path: "/",
        element: <Root />,
        children: [
            {
                path: "/",
                element: <Home />,
            },
            {
                path: "myself",
                element: <Users />,
            },
            {
                path: "about",
                element: <About />,
            },
            {
                path: 'story/:storyId',
                element: <Story />
            }
        ]
    },

]);

export default router;