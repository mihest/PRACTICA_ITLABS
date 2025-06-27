import {useEffect, useState} from "react";


const FilterPanel = ({open, setOpen}) => {
    const [filters, setFilters] = useState([])

    useEffect(() => {
        const fetchFilters = async () => {
            try {
                const res = await fetch(import.meta.env.VITE_API_URL + "/members/filters/get");
                const data = await res.json();
                setFilters(data);
                console.log(filters)
            } catch (e) {
                console.log(e)
                alert("Ошибка загрузки данных " + e.message);
            }
        };
        fetchFilters();
    })

    if (!open) return null
    return (
        <>
            <div className="absolute top-0 left-0 py-[40px] ps-[80px] pe-[40px] w-[508px] h-[1080px]">
                <div className="w-full">
                    <div className="flex w-full">
                        <span className="uppercase text-[#514F4D] text-[40px]/[46px] font-[400]">Фильтры</span>
                    </div>
                </div>
            </div>
            <div />
        </>
    )
};

export default FilterPanel;