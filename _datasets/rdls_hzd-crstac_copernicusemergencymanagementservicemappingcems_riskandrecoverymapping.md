---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: CEMS
  url: https://mapping.emergency.copernicus.eu/
creator:
  affiliation: null
  email: null
  name: CEMS
  url: https://mapping.emergency.copernicus.eu/
dataset_id: rdls_hzd-crstac_copernicusemergencymanagementservicemappingcems_riskandrecoverymapping
description: 'This service provides on-demand geospatial information to support emergency
  management activities outside the immediate response phase. It covers the prevention,
  preparedness, disaster risk reduction, and recovery phases [Source: This metadata
  record was automatically extracted from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
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
      intensity_measure: burnedarea:ha
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: wildfire
license: https://example.org/license/unknown
lineage:
  description: 'The Copernicus Emergency Management Service (CEMS) uses satellite
    imagery and other geospatial data to provide free of charge mapping service in
    cases of natural disasters, human-made emergency situations and humanitarian crises
    throughout the world. It covers the following hazards relevant for climate risk
    assessments: floods, severe storms, fires'
  sources:
  - id: source_underlying_1
    license: null
    name: satellite imagery and local data
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: CEMS
  url: https://mapping.emergency.copernicus.eu/
purpose: Download per event/case study possible
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: ref_pub_publicationlink
  name: Publication link
  url: https://mapping.emergency.copernicus.eu/about/risk-and-recovery-manual/
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/environmental/copernicus-emergency-management-service-mapping-cems/risk-and-recovery-mapping/risk-and-recovery-mapping.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Item metadata record for this dataset, hosted as part of
    the climate-risk-stac catalogue. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_item
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: event level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Item: Copernicus Emergency Management Service - Mapping (CEMS) - Risk
    and recovery mapping'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Copernicus Emergency Management Service - Mapping (CEMS) - Risk and
    recovery mapping - data file
  download_url: https://mapping.emergency.copernicus.eu/activations/
  format: null
  id: resource_data-file_1
  media_type: application/x-shapefile
  spatial: null
  spatial_aggregation: event level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Copernicus Emergency Management Service - Mapping (CEMS) - Risk and recovery
    mapping - data file
- access_url: https://mapping.emergency.copernicus.eu/about/risk-and-recovery-manual/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Emergency Management Service - Mapping (CEMS) - Risk and
    recovery mapping (Publication link)
  download_url: null
  format: Web reference
  id: resource_link_publicationlink
  media_type: null
  spatial: null
  spatial_aggregation: event level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Publication link
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-crstac_copernicusemergencymanagementservicemappingcems_riskandrecoverymapping
spatial:
  bbox:
  - -180.0
  - -90.0
  - 180.0
  - 90.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026'
  start: '2017'
temporal_resolution: null
title: Copernicus Emergency Management Service - Mapping (CEMS) - Risk and recovery
  mapping
version: null
vulnerability: null
---
