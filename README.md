# NeuroAI: Deep Brain Stimulation Electrode Optimization

A machine learning project to assist in optimizing electrode placement in DBS procedures by identifying neuroanatomical patterns associated with Parkinson's Disease. Though the project was ultimately discontinued, it represents an early exploration into applying AI to neuroimaging and surgical planning.

## Summary
- Goal: Reduce postoperative infection by minimizing intraoperative time
- Approach: Random Forest classification of T1-weighted MRI scans
- Tools: ITK-SNAP for segmentation, Harvard-Oxford Atlas, Scikit-learn
- Status: Discontinued – code and notes archived for reference

## File Structure
- `notebooks/`: Experimental model training
- `src/`: Scripts for segmentation, feature extraction, and classification
- `data/`: Expected structure for T1 scans
- `atlas/`: Reference atlas information

## Neuroimaging Resources

This project references the following brain atlas:

- [Harvard-Oxford Cortical and Subcortical Structural Atlases](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Atlases)
  - Provided by the FMRIB Software Library (FSL)
  - Used for identifying regions such as the substantia nigra, thalamus, and basal ganglia
- [ITK-SNAP](http://www.itksnap.org/pmwiki/pmwiki.php)
  - Used for manual and semi-automatic segmentation of T1-weighted MRI scans

## Notes
This repository is for documentation/reference purposes and does not contain medical advice or deployable clinical tools.
