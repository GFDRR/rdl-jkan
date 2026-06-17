---
attributions:
- entity:
    affiliation: null
    email: null
    name: Tropical Storm Risk, University College London
    url: https://data.humdata.org/dataset/hurricane-matthew-gust-footprint-tropical-storm-risk-university-college-london
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: British Red Cross Maps Team
  url: https://data.humdata.org/dataset/hurricane-matthew-gust-footprint-tropical-storm-risk-university-college-london
creator:
  affiliation: null
  email: null
  name: British Red Cross Maps Team
  url: https://data.humdata.org/dataset/hurricane-matthew-gust-footprint-tropical-storm-risk-university-college-london
dataset_id: rdls_hzd-hti_brc_hurricanematthewgustfootp_20161006
description: 'Tropical Storm Risk - University College London - gust footprint for
  Matthew in kml format. If you zoom in (using Google Earth) the footprint shows the
  towns and villages in western Haiti which UCL model predicts will be worst affected
  by wind damage (with peak gusts of 160 mph (260 kmph)).. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hurricane-matthew-gust-footprint-tropical-storm-risk-university-college-london]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: PGWS:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: strong_wind
license: CC-BY-4.0
lineage:
  description: The Tropical Storm Risk model at University College London simulated
    wind gust patterns for Hurricane Matthew using their established tropical cyclone
    hazard methodology. The model output was processed into spatial footprint geometries
    (KML and shapefile formats) delineating areas in western Haiti predicted to experience
    peak gusts of 260 kmph, enabling identification of towns and villages at highest
    risk of wind damage.
  sources:
  - id: source_1
    license: null
    name: Tropical Storm Risk, University College London
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hurricane-matthew-gust-footprint-tropical-storm-risk-university-college-london
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: http://www.ucl.ac.uk/mssl/climate-extremes
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Haiti - Hurricane Matthew gust footprint - Tropical Storm Risk, University
    College London (KML file for Google Earth)
  download_url: https://data.humdata.org/dataset/b6656951-f517-4d8e-97aa-db538bedde70/resource/49e7ad9e-7258-4b06-8529-0787bdf0f740/download/hurricane-matthew-gust-footprint-tsrucl.kml
  format: null
  id: resource_49e7ad9e
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Hurricane Matthew gust footprint-TSRUCL.kml
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Haiti - Hurricane Matthew gust footprint - Tropical Storm Risk, University
    College London (Zipped shapefile for GIS softwares)
  download_url: https://data.humdata.org/dataset/b6656951-f517-4d8e-97aa-db538bedde70/resource/d80e569f-7834-487b-98d7-4ee7f83bb192/download/hurricane-matthew-gust-footprint-tsrucl.zip
  format: null
  id: resource_d80e569f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Hurricane-Matthew-gust-footprint-TSRUCL.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-hti_brc_hurricanematthewgustfootp_20161006
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-10-06'
temporal_resolution: null
title: Haiti - Hurricane Matthew gust footprint - Tropical Storm Risk, University
  College London
version: null
vulnerability: null
---
