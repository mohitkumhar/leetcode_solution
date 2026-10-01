struct stack
{
    int size;
    int top;
    int *arr;
};

int isEmpty(struct stack *sp)
{
    return sp->top == -1;
}

void push(struct stack *sp, int data)
{
    if (sp->top == sp->size - 1)
        return;

    sp->top++;
    sp->arr[sp->top] = data;
}

int pop(struct stack *sp)
{
    if (isEmpty(sp))
        return -1;

    int popedValue;
    popedValue = sp->arr[sp->top];
    sp->top--;

    return popedValue;
}

bool isValid(char* s) {
    struct stack *sp = (struct stack *)malloc(sizeof(struct stack));
    sp->size = 1000000;
    sp->top = -1;
    sp->arr = (int *)malloc(sp->size * sizeof(int));

    int i = 0;
    while (s[i] != '\0')
    {

        // Pushing Value into Stack
        if (s[i] == '{' || s[i] == '[' || s[i] == '(')
        {
            push(sp, s[i]);
        }

        // Poping Values From Stack
        else
        {
            int popedValue = pop(sp);

            if (s[i] == ']' && popedValue != '[' ||
                s[i] == '}' && popedValue != '{' ||
                s[i] == ')' && popedValue != '(')
                return 0;
        }
        i++;
    }
    
    if(isEmpty(sp))
    {
        return 1;
    }
    return 0;
}