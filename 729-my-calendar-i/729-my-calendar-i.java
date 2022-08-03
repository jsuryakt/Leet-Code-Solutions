class MyCalendar {
    
    ArrayList<ArrayList<Integer>> calendar;
    
    public MyCalendar() {
        calendar = new ArrayList<ArrayList<Integer>>();    
    }
    
    public boolean book(int start, int end) {
        for(ArrayList<Integer> event: calendar) {
            if(start<event.get(1) && end>event.get(0)) {
                return false;
            }
        }
        calendar.add(new ArrayList(Arrays.asList(start, end)));
        return true;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */