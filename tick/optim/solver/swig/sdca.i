// License: BSD 3 clause

%include <std_shared_ptr.i>

%{
#include "sdca.h"
#include "model.h"
%}

enum class BatchSize {
  one = 0,
  two,
  many
};

class SDCA : public StoSolver {

public:

    SDCA(double l_l2sq,
         unsigned long epoch_size = 0,
         double tol = 0.,
         RandType rand_type = RandType::unif,
         BatchSize batch_size = BatchSize::one,
         ulong batch_number = 1,
         int seed = -1);

    void set_model(std::shared_ptr<Model> model);

    void set_prox(std::shared_ptr<Prox> prox);

    void reset();

    void set_starting_iterate();
    void set_starting_iterate(ArrayDouble &dual_vector);

    void solve();

    double get_l_l2sq() const;

    void set_l_l2sq(double l_l2sq);

    SArrayDoublePtr get_primal_vector();
    SArrayDoublePtr get_dual_vector();
};
