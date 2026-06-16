---
attributions:
- entity:
    affiliation: null
    email: null
    name: Climatic Research Unit (University of East Anglia)
    url: https://data.humdata.org/dataset/global-droughts-events-1980-2001
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: International Research Institute for Climate and Society (IRI, Columbia
      University)
    url: https://data.humdata.org/dataset/global-droughts-events-1980-2001
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/global-droughts-events-1980-2001
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/global-droughts-events-1980-2001
dataset_id: rdls_hzd-undrr_globaldroughtsevents_1980
description: 'This dataset includes an estimate of global drought annual repartition
  based on Standardized Precipitation Index. It is based on two sources: 1) A global
  monthly gridded precipitation dataset obtained from the Climatic Research Unit (University
  of East Anglia). 2) A GIS modeling of global Standardized Precipitation Index based
  on Brad Lyon (IRI, Columbia University) methodology. This product was designed by
  UNEP/GRID-Europe for the Project of Risk Evaluation, Vulnerability, Information
  & Early Warning (PreView). It was modeled using global data. Credit: UNEP/GRID-Europe.
  [Preview this dataset] (http://preview.grid.unep.ch/index.php?preview=data&events=droughts&evcat=1&lang=eng).
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/global-droughts-events-1980-2001]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: simulated
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
license: CC-BY-4.0
lineage:
  description: Global monthly gridded precipitation data from the Climatic Research
    Unit was processed using the Standardized Precipitation Index methodology (Brad
    Lyon, IRI) via GIS modeling to estimate annual drought event distribution worldwide.
    The dataset was developed by UNEP/GRID-Europe for the PreView project to support
    risk evaluation and early warning.
  sources:
  - id: source_1
    license: null
    name: Climatic Research Unit (University of East Anglia)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: International Research Institute for Climate and Society (IRI, Columbia
      University)
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/global-droughts-events-1980-2001
  rel: source
loss: null
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
  description: Zipped shapefile of droughts events from 1980 to 2001. (15,637 kb)
  download_url: https://data.humdata.org/dataset/f5e8b21e-bb71-40e3-8129-5378ebc42e33/resource/52263859-fdfa-4622-bfb0-34ba82cc6729/download/dr-events-20150505221917-shapefile.zip
  format: null
  id: resource_52263859
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dr-events-20150505221917-shapefile.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global droughts events (CSV files of drought events from 1980 to 2001
    (1,704 kb))
  download_url: https://data.humdata.org/dataset/f5e8b21e-bb71-40e3-8129-5378ebc42e33/resource/222389aa-9089-428d-8d60-1f6895df6618/download/dr-events.csv
  format: null
  id: resource_222389aa
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dr_events.csv
- access_url: http://preview.grid.unep.ch/index.php?preview=data&events=droughts&evcat=1&lang=eng
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global droughts events (Url link to drought events 1980-2001.)
  download_url: null
  format: null
  id: resource_e83b61bf
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Url link to drought events 1980-2001.
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-undrr_globaldroughtsevents_1980
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2001-12-31'
  start: '1980-01-01'
temporal_resolution: null
title: Global droughts events
version: null
vulnerability: null
---
