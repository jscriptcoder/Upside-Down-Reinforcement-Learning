import torch

# https://arxiv.org/pdf/1912.02877.pdf

class Behavior(torch.nn.Module):
    # 3.2 Setup
    def __init__(self, 
                 state_size, 
                 action_size, 
                 hidden_size, 
                 command_scale = [1, 1]):
        super().__init__()
        
        self.command_scale = torch.FloatTensor(command_scale)
        
        self.state_fc = torch.nn.Sequential(torch.nn.Linear(state_size, 
                                                            hidden_size), 
                                            torch.nn.Sigmoid())
        
        self.command_fc = torch.nn.Sequential(torch.nn.Linear(2, hidden_size), 
                                              torch.nn.Sigmoid())
        
        self.output_fc = torch.nn.Sequential(torch.nn.Linear(hidden_size, 
                                                             hidden_size), 
                                             torch.nn.ReLU(), 
                                             torch.nn.Linear(hidden_size, 
                                                             action_size))
        
    
    def forward(self, state, command):
        
        state_output = self.state_fc(state)
        command_output = self.command_fc(command * self.command_scale)
        
        embedding = torch.mul(state_output, command_output)
        
        return self.output_fc(embedding)