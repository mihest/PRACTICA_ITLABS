const Loader = ({className}) => {
    return (
        <div
            className={`fixed inset-0 bg-black/80 flex items-center justify-center z-50 ${className}`}
        >
            <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 200 200"
                className="text-white h-[100px]"
            >
                <circle
                    fill="currentColor"
                    stroke="currentColor"
                    strokeWidth="15"
                    r="15"
                    cx="40"
                    cy="65"
                >
                    <animate
                        attributeName="cy"
                        calcMode="spline"
                        dur="2s"
                        values="65;135;65;"
                        keySplines=".5 0 .5 1;.5 0 .5 1"
                        repeatCount="indefinite"
                        begin="-.4s"
                    />
                </circle>
                <circle
                    fill="currentColor"
                    stroke="currentColor"
                    strokeWidth="15"
                    r="15"
                    cx="100"
                    cy="65"
                >
                    <animate
                        attributeName="cy"
                        calcMode="spline"
                        dur="2s"
                        values="65;135;65;"
                        keySplines=".5 0 .5 1;.5 0 .5 1"
                        repeatCount="indefinite"
                        begin="-.2s"
                    />
                </circle>
                <circle
                    fill="currentColor"
                    stroke="currentColor"
                    strokeWidth="15"
                    r="15"
                    cx="160"
                    cy="65"
                >
                    <animate
                        attributeName="cy"
                        calcMode="spline"
                        dur="2s"
                        values="65;135;65;"
                        keySplines=".5 0 .5 1;.5 0 .5 1"
                        repeatCount="indefinite"
                        begin="0s"
                    />
                </circle>
            </svg>
        </div>
    );
};

export default Loader;
