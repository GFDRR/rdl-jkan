---
attributions:
- entity:
    affiliation: null
    email: null
    name: MODIS
    url: https://data.humdata.org/dataset/central-america-crops-vegetation-and-precipitation-index
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: CHIRPS
    url: https://data.humdata.org/dataset/central-america-crops-vegetation-and-precipitation-index
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/central-america-crops-vegetation-and-precipitation-index
creator:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/central-america-crops-vegetation-and-precipitation-index
dataset_id: rdls_hzd-achgis4tech_centralamericacropsvegeta_2020
description: 'Database containing information related to precipitation indices useful
  for analysing and comparing variations in precipitation over time and in different
  geographical regions and indices used in the analysis of vegetation and crops to
  monitor their activity and detect their presence in the territory. Key variables:
  Atmospherically Resistant Vegetation Index (ARVI), Normalized Difference Vegetation
  (NDVI), Enhanced Vegetation Index (EVI) and Structure Insensitive Pigment Index
  (SIPI) for rainfall information and Standardized Precipitation Index (SPI1, SPI3,
  SPI6, SPI9 and SPI12) for vegetation information. The indicators between SPI1 -
  SPI3 refer to short time periods (indicator for immediate impacts) while SPI3 -
  SPI12 is for more medium-term impact measurements. Each vegetation index is based
  on a set of data that can be collected through remote sensing, such as satellite
  imagery, and is designed to measure different vegetation and crop characteristics.
  The data are categorised by country, department and municipality and by year and
  month. The indices refer to the monthly average. Vegetation and precipitation data
  have been produced and transformed by GIS4Tech. For more information contact GIS4Tech:
  info@gis4tech.com. You can also visit the PREDISAN platform: https://predisan.gis4tech.com/ca4.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/central-america-crops-vegetation-and-precipitation-index]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    drought:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: SPI:-
        process: meteorological_drought
        trigger: null
        type: drought
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Monthly vegetation and precipitation indices were derived from MODIS
    and CHIRPS satellite data collected from 2020 onwards. Vegetation indices (NDVI,
    EVI, ARVI, SIPI) and Standardized Precipitation Index (SPI) at multiple timescales
    were calculated and aggregated to municipal level using median values across each
    geographic area to monitor drought conditions and crop/vegetation activity in
    Central America.
  sources:
  - id: source_1
    license: null
    name: MODIS
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: CHIRPS
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/central-america-crops-vegetation-and-precipitation-index
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Central America Monthly Crops Vegetation and Precipitation Index since
    2020 by ACH-GIS4Tech.csv
  download_url: https://data.humdata.org/dataset/9af68a9c-c7a9-4ce7-afdd-bf23e2c48ae5/resource/8cc5b059-5976-4901-8375-b580ad628622/download/spi_crops.csv
  format: null
  id: resource_8cc5b059
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Central America Monthly Crops Vegetation and Precipitation Index since 2020
    by ACH-GIS4Tech.csv
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-achgis4tech_centralamericacropsvegeta_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - GTM
  - HND
  - SLV
  - NIC
  - CRI
  - PAN
  - BLZ
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-01'
  start: '2020-01-01'
temporal_resolution: null
title: Central America - Crops Vegetation and Standardized Precipitation Index
version: null
vulnerability: null
---
