---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: science@axaclimate.com
  name: AXA Climate
  url: null
creator:
  affiliation: null
  email: null
  name: AXA Climate
  url: https://climate.axa
dataset_id: rdls_hzd-mdg_grma_winderosion
description: Wind erodible fraction analysis examining soil texture and chemical properties
  to identify dust storm emission sources across Madagascar.
details: The wind erodible fraction examines the top 0-5 cm layer of soil's texture
  and chemical properties, indicates the soil susceptibility to erosion. The soil
  erodible fraction is determined based on the methodology developed by Fryrear et
  al. (1994) and data extracted from the SoilGrids database (Hengl et al., 2017).
  The wind erodible fraction is overlayed with the bare soil and shrubland locations
  to highlight potential dust storm emission sources.
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_erosion_001
      intensity_measure: MHI:-
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_erosion_001
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: GRMA Madagascar - Phase 1
  url: https://www.resiliencemada.gov.mg
publisher:
  affiliation: null
  email: null
  name: Global Risk Modelling Alliance
  url: https://grma.global
purpose: This dataset was developed during the first phase of GRMA's project in Madagascar.
  This project aimed at updating Madagascar's risk profile, and see the risk evolution
  under climate change.
referenced_by:
- author_names:
  - "Tomislav Hengl ,Jorge Mendes de Jesus,Gerard B. M. Heuvelink,Maria Ruiperez Gonzalez,Milan\
    \ Kilibarda,Aleksandar Blagoti\xC4\u2021,Wei Shangguan,Marvin N. Wright,Xiaoyuan\
    \ Geng,Bernhard Bauer-Marschallinger,Mario Antonio Guevara,Rodrigo Vargas,Robert\
    \ A. MacMillan,Niels H. Batjes,Johan G. B. Leenaars,Eloi Ribeiro,Ichsani Wheeler,Stephan\
    \ Mantel,Bas Kempen"
  date_published: '2017-02-16'
  doi: https://doi.org/10.1371/journal.pone.0169748
  id: reference_3XRpJO6G
  name: 'SoilGrids 250m: Global gridded soil information based on machine learning'
  url: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0169748
- author_names:
  - 'Fryrear, D. W., Krammes, C. A., Williamson, D. L., & Zobeck, T. M. '
  date_published: null
  doi: https://doi.org/10.1080/00224561.1994.12456849
  id: reference_JnvdOSMe
  name: Computing the wind erodible fraction of soils
  url: tandfonline.com/doi/abs/10.1080/00224561.1994.12456849
resources:
- access_url: https://soilgrids.org/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: SoilGrids is a system for global digital soil mapping that uses state-of-the-art
    machine learning methods to map the spatial distribution of soil properties across
    the globe.
  download_url: https://soilgrids.org/
  format: null
  id: resource_szweUR0z
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 1000
  temporal: null
  temporal_resolution: null
  title: SoilGrids database
- access_url: https://www.resiliencemada.gov.mg/catalogue/#/dataset/1162
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: High resolution land cover from ESA's WorldCover data v200. The bare/sparse
    vegetation and shrubland grid points are extracted to describe regions that can
    become dust emission sources.
  download_url: https://www.resiliencemada.gov.mg/catalogue/#/dataset/1162
  format: null
  id: resource_XRXrhsbL
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 10
  temporal:
    central_year: null
    duration: null
    end: '2021'
    start: '2021'
  temporal_resolution: null
  title: Bare soil and shrubland
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mdg_grma_winderosion
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Wind erosion
version: '1.0'
vulnerability: null
---
