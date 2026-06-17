---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1
    url: https://data.humdata.org/dataset/mozambique-flood-detected-waters-cyclone-idai
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Copernicus
    url: https://data.humdata.org/dataset/mozambique-flood-detected-waters-cyclone-idai
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Atmospheric and Environmental Research (A Verisk Business)
    url: https://data.humdata.org/dataset/mozambique-flood-detected-waters-cyclone-idai
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: African Risk Capacity
    url: https://data.humdata.org/dataset/mozambique-flood-detected-waters-cyclone-idai
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/mozambique-flood-detected-waters-cyclone-idai
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/mozambique-flood-detected-waters-cyclone-idai
dataset_id: rdls_hzd-moz_wfp_satellitedetectedwaterscy_20190321
description: 'This dataset is a compilation of various sources such as Copernicus,
  Sentinel-1 and Atmospheric and Environmental Research, A Verisk Business, & African
  Risk Capacity using several days to calculate the maximum flood extent for the whole
  event.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mozambique-flood-detected-waters-cyclone-idai]'
details: 'Disclaimer for Flood depictions: AFED v05r00 The ARC Flood Extent Depiction
  (AFED) data have been developed by Atmospheric Environmental Research, Inc. (AER),
  a Verisk Business, for the African Risk Capacity (ARC) Group. AFED data are downscaled
  from coarse resolution (22 km) microwave satellite data and, although depicted at
  ~90m resolution, will only detect large scale river flooding. Flooding in elevated
  areas and small tributaries usually is not detected. The data are provided to the
  public for information purposes only, and neither AER nor the ARC Group make any
  representation or warranty regarding the fitness of the data and information for
  any particular purpose. In no event shall AER nor the ARC Group be held liable with
  respect to any subject matter presented here.'
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: Multi-temporal satellite observations from Sentinel-1 SAR and Copernicus
    data collected over several days during Cyclone Idai were processed using the
    AFED v05r00 flood detection algorithm to delineate maximum inundation extent.
    The resulting flood extent polygons represent observed water surfaces derived
    from direct satellite observation rather than hydrological modeling.
  sources:
  - id: source_1
    license: null
    name: Sentinel-1
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Copernicus
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_3
    license: null
    name: Atmospheric and Environmental Research (A Verisk Business)
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_4
    license: null
    name: African Risk Capacity
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mozambique-flood-detected-waters-cyclone-idai
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood extent as of 12 March. Compiled from Copernicus and Sentinel
    1
  download_url: https://data.humdata.org/dataset/4b3930dc-21a4-43b3-9257-e1f552a969a6/resource/3f2b3a74-e5dc-44d3-a339-007a1396bf0a/download/moz_floods_20190312.zip
  format: null
  id: resource_3f2b3a74
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MOZ_floods_20190312.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Maximum flood extent as of 21 March. Compiled from Copernicus, Sentinel
    1 using data from 12 to 21 March 2019 and AFED-detected non-persistent water (7-16
    March and 20 March 2019)
  download_url: https://data.humdata.org/dataset/4b3930dc-21a4-43b3-9257-e1f552a969a6/resource/9a3f23c6-0cc3-4e99-bb72-0b4e099847df/download/moz_totalfloodextent.zip
  format: null
  id: resource_9a3f23c6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MOZ_TotalFloodExtent.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-moz_wfp_satellitedetectedwaterscy_20190321
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-03-21'
temporal_resolution: null
title: Mozambique satellite detected waters, Cyclone Idai
version: null
vulnerability: null
---
