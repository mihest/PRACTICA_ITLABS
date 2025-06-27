import {useContext, useEffect, useState} from "react";
import {LoadingContext} from "../context/LoadingContext.jsx";
import HeroGrid from "../components/HeroGrid.jsx";


const HomePage = () => {
    const { loading, setLoading } = useContext(LoadingContext);
    const [members, setMembers] = useState([]);

    useEffect(() => {
        const fetchMember = async () => {
            try {
                const res = await fetch(import.meta.env.VITE_API_URL + "/members");
                const data = await res.json();
                setMembers(data);
            } catch (e) {
                console.log(e)
                alert("Ошибка загрузки данных " + e.message);
            } finally {
                setLoading(false);
            }
        };
        fetchMember();
    }, [setLoading]);
    if (loading) return null;
    return (
        <div className="mt-[52px] w-full">
            <div className="flex gap-[16px] ms-[80px]">
                <button className="bg-[#CF3337] w-[280px] h-[69px] flex items-center justify-center gap-[19px] cursor-pointer">
                    <img src="/search.svg" alt="Search" />
                    <span className="text-white text-[18px]/[21px] font-[400] uppercase">Поиск героя</span>
                </button>
                <button className="border-[1px] border-[#514F4D] w-[280px] h-[69px] flex items-center justify-center gap-[19px] cursor-pointer">
                    <img src="/filter.svg" alt="Filter" />
                    <span className="text-[#514F4D] text-[18px]/[21px] font-[400] uppercase">Фильтр</span>
                </button>
                <div className="flex items-center gap-[20px] flex-1">
                    <span className="text-[#514F4D] text-[40px]/[46px] font-[400] uppercase">Стена памяти</span>
                    <img src="/scroll.svg" alt="Scroll" className="flex-1" />
                </div>
            </div>
            <HeroGrid members={members}/>
            
        </div>
    )
}

export default HomePage;