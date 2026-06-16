---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme (WFP)
    url: https://data.humdata.org/dataset/cambodia-other-0-0-0
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Cambodia Humanitarian Response Forum (HRF)
    url: https://data.humdata.org/dataset/cambodia-other-0-0-0
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Regional Office for Asia and the Pacific (ROAP)
  url: https://data.humdata.org/dataset/cambodia-other-0-0-0
creator:
  affiliation: null
  email: null
  name: OCHA Regional Office for Asia and the Pacific (ROAP)
  url: https://data.humdata.org/dataset/cambodia-other-0-0-0
dataset_id: rdls_hzd-khm_ocharoap_floodextent2013_20131007
description: 'Cambodia flood extent in 2013. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/cambodia-other-0-0-0]'
details: "**Languages:** EN The flood extent was based on a preliminary analysis of\
  \ SAR satellite imagery of COSMO-SkyMed (csk) acquired on 08 and 09 Oct 2013 and\
  \ RADARSAT-2 (rs2) acquired on 09 Oct 2013. The analysis was done by Copernicus\
  \ Emergency Management Service-Mapping \xC2\xA9 European Commission and has not\
  \ been validated in the field yet."
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
license: CC-BY-4.0
lineage:
  description: Flood extent was mapped from remote sensing imagery (GIOEMS/CSK/RS2)
    acquired during the October 2013 flood event in Cambodia. The shapefile represents
    the observed spatial extent of inundation derived from satellite data processing
    by WFP and HRF.
  sources:
  - id: source_1
    license: null
    name: World Food Programme (WFP)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Cambodia Humanitarian Response Forum (HRF)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cambodia-other-0-0-0
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
  description: Cambodia - Flood extent in 2013 (Shapefile)
  download_url: https://data.humdata.org/dataset/e2e51702-a126-4da4-8b56-fd474c27ac9a/resource/1ffbde56-41a5-4086-875a-6ec8a1d2de86/download/khm_fldextenta_gioems_csk_rs2_2013100809.zip
  format: null
  id: resource_1ffbde56
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: khm_fldextenta_gioems_csk_rs2_2013100809.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-khm_ocharoap_floodextent2013_20131007
spatial:
  bbox: null
  centroid: null
  countries:
  - KHM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2013-10-07'
temporal_resolution: null
title: Cambodia - Flood extent in 2013
version: null
vulnerability: null
---
