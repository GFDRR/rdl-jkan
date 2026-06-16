---
attributions:
- entity:
    affiliation: null
    email: null
    name: GFDRR
    url: https://www.gfdrr.org
  id: '1'
  role: resource_provider
- entity:
    affiliation: null
    email: null
    name: ARUP
    url: https://www.arup.com
  id: '2'
  role: author
catalog: World Bank Data Catalog
contact_point:
  affiliation: null
  email: mamadio@worldbank.org
  name: Mattia Amadio
  url: null
creator:
  affiliation: null
  email: null
  name: ARUP
  url: https://www.arup.com
dataset_id: rdls_hzd-arup_globallandslidehazardmaps
description: The Global Landslide hazard map is a gridded dataset of landslide hazard
  produced at the global scale. Landslides happen around the world and have devastating
  impacts on people and the built environment. To better understand the spatial and
  temporal distribution of landslide hazard worldwide, the World Bank and the Global
  Facility for Disaster Reduction and Recovery (GFDRR) commissioned Arup to undertake
  a landslide hazard assessment at a global scale. Using a global landslide inventory,
  landslide susceptibility information provided by NASA, and an innovative machine
  learning model, our geohazard and risk management experts produced a state-of-the-art
  quantitative landslide hazard map for the whole world.
details: "The dataset comprises gridded maps of estimated annual frequency of significant\
  \ landslides per square kilometre. Significant landslides are those which are likely\
  \ to have been reported had they occurred in a populated place; limited information\
  \ on reported landslide size makes it difficult to tie frequencies to size ranges\
  \ but broadly speaking would be at least greater than 100 m2. The data provides\
  \ frequency estimates for each grid cell on land between 60\xB0S and 72\xB0N for\
  \ landslides triggered by seismicity and rainfall. Applications of this dataset\
  \ include improved hazard screening based on frequency and severity, consistent\
  \ national, regional and global scale exposure assessment, estimates of annual expected\
  \ impact on population and the built environment."
exposure: []
hazard:
  event_sets_by_hazard_type:
    landslide:
    - analysis_type: deterministic
      calculation_method: inferred
      event_count: 400000
      events:
      - calculation_method: inferred
        description: null
        disaster_identifiers: []
        hazard:
          classification: null
          id: RF
          intensity_measure: ls_hzd:-
          process: landslide_general
          trigger:
            process: null
            type: convective_storm
          type: landslide
        id: '1'
        occurrence:
          deterministic:
            description: null
            index_criteria: Median
            thresholds:
            - '0.001'
            - '0.01'
          empirical: null
          probabilistic: null
      frequency_distribution: user_defined
      hazards:
      - classification: null
        id: RF
        intensity_measure: ls_hzd:-
        process: landslide_general
        trigger:
          process: null
          type: convective_storm
        type: landslide
      id: RF_trigger-med
      occurrence_range: null
      seasonality: uniform
    - analysis_type: deterministic
      calculation_method: inferred
      event_count: 400000
      events:
      - calculation_method: inferred
        description: null
        disaster_identifiers: []
        hazard:
          classification: null
          id: RF
          intensity_measure: ls_hzd:-
          process: landslide_general
          trigger:
            process: null
            type: convective_storm
          type: landslide
        id: '1'
        occurrence:
          deterministic:
            description: null
            index_criteria: Mean
            thresholds:
            - '0.001'
            - '0.01'
          empirical: null
          probabilistic: null
      frequency_distribution: user_defined
      hazards:
      - classification: null
        id: RF
        intensity_measure: ls_hzd:-
        process: landslide_general
        trigger:
          process: null
          type: convective_storm
        type: landslide
      id: RF_trigger-mea
      occurrence_range: null
      seasonality: uniform
    - analysis_type: deterministic
      calculation_method: inferred
      event_count: 130000
      events:
      - calculation_method: inferred
        description: null
        disaster_identifiers: []
        hazard:
          classification: null
          id: EQ
          intensity_measure: ls_hzd:-
          process: landslide_general
          trigger:
            process: null
            type: earthquake
          type: landslide
        id: '1'
        occurrence:
          deterministic:
            description: null
            index_criteria: Median
            thresholds:
            - '0.001'
            - '0.01'
          empirical: null
          probabilistic: null
      frequency_distribution: user_defined
      hazards:
      - classification: null
        id: EQ
        intensity_measure: ls_hzd:-
        process: landslide_general
        trigger:
          process: null
          type: earthquake
        type: landslide
      id: EQ_trigger
      occurrence_range: null
      seasonality: uniform
  event_sets_count: 3
license: CC-BY-4.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: GFDRR
  url: https://www.gfdrr.org
purpose: null
referenced_by:
- author_names:
  - Peter Redshaw
  - James Bottomley
  - Matthew Free
  date_published: '2021-04-29'
  doi: null
  id: '1'
  name: Global Landslide Hazard map - Project report
  url: https://datacatalogfiles.worldbank.org/ddh-published/0037584/DR0045411/global-landslide-hazard-map-report.pdf?versionId=2023-01-18T20:43:00.6156776Z
resources:
- access_url: https://datacatalog.worldbank.org/search/dataset/0037584/global-landslide-hazard-map
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Median global landslide hazard triggered by heavy rainfall trigger
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0037584/DR0045414/ls_rf_median_1980-2018.zip
  format: geotiff
  id: RF_trigger-med
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 1000
  temporal: null
  temporal_resolution: null
  title: Median rainfall landslide hazard
- access_url: https://datacatalog.worldbank.org/search/dataset/0037584/global-landslide-hazard-map
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Mean global landslide hazard triggered by heavy rainfall trigger
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0037584/DR0045413/ls_rf_mean_1980-2018.zip
  format: geotiff
  id: RF_trigger-mea
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 1000
  temporal: null
  temporal_resolution: null
  title: Mean rainfall landslide hazard
- access_url: https://datacatalog.worldbank.org/search/dataset/0037584/global-landslide-hazard-map
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Mean global landslide hazard triggered by earthquake
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0037584/DR0045412/ls_eq.zip
  format: geotiff
  id: EQ_trigger
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 1000
  temporal: null
  temporal_resolution: null
  title: Global landslide hazard triggered by earthquake (median)
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-arup_globallandslidehazardmaps
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Global landslide hazard maps
version: '1'
vulnerability: null
---
