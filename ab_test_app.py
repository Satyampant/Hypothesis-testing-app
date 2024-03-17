import scipy.stats as stats


def perform_ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions,
                    confidence_level=95):
    # Calculate conversion rates
    control_rate = control_conversions / control_visitors
    treatment_rate = treatment_conversions / treatment_visitors

    # Perform two-sample t-test
    t_stat, p_value = stats.ttest_ind_from_stats(
        mean1=control_rate,
        std1=0,  # We assume equal variance for simplicity
        nobs1=control_visitors,
        mean2=treatment_rate,
        std2=0,
        nobs2=treatment_visitors
    )

    # Determine significance based on confidence level
    alpha = (100 - confidence_level) / 100
    if p_value < alpha:
        if treatment_rate > control_rate:
            return "Experiment Group is Better"
        else:
            return "Control Group is Better"
    else:
        return "Indeterminate"


import streamlit as st
#from hypothesis_testing_function import perform_ab_test

# Define the Streamlit app
def main():
    st.title("A/B Test Hypothesis Testing App")

    # Input parameters
    st.sidebar.header("Input Parameters")
    control_visitors = st.sidebar.number_input("Control Group Visitors", min_value=1, step=1)
    control_conversions = st.sidebar.number_input("Control Group Conversions", min_value=0, step=1)
    treatment_visitors = st.sidebar.number_input("Treatment Group Visitors", min_value=1, step=1)
    treatment_conversions = st.sidebar.number_input("Treatment Group Conversions", min_value=0, step=1)
    confidence_level = st.sidebar.select_slider("Confidence Level", options=[90, 95, 99])

    # Perform A/B test
    result = perform_ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level)

    # Display result
    st.subheader("A/B Test Result:")
    st.write(result)

# Run the app
if __name__ == "__main__":
    main()

