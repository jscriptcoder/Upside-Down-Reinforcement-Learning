import torch

class Behavior(nn.Module):
    def __init__(self, 
                 state_size, 
                 action_size, 
                 hidden_size, 
                 command_scale = (1, 1)):
        super().__init__()
        
        self.command_scale = command_scale
        self.state_fc = torch.nn.Sequential(torch.nn.Linear(state_size, hidden_size), 
                                            torch.nn.Sigmoid())
        self.command_fc = torch.nn.Sequential(torch.nn.Linear(2, hidden_size), 
                                              torch.nn.Sigmoid())
        
    
    def forward(self, state, command):
        state_output = self.state_fc(state)
        command_output = self.command_fc(command * self.command_scale)
        output = torch.mul(state_output, command_output)