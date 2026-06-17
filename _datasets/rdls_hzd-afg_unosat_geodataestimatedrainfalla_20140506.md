---
attributions:
- entity:
    affiliation: null
    email: null
    name: Tropical Rainfall Monitoring Mission (TRMM)
    url: https://data.humdata.org/dataset/geodata-of-estimated-rainfall-accumulation-from-30-april-to-06-may-2014-afgha-may-06-2014
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-estimated-rainfall-accumulation-from-30-april-to-06-may-2014-afgha-may-06-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-estimated-rainfall-accumulation-from-30-april-to-06-may-2014-afgha-may-06-2014
dataset_id: rdls_hzd-afg_unosat_geodataestimatedrainfalla_20140506
description: 'This map presents the estimated total rainfall accumulation for Afghanistan
  covering the period from 30 April to 06 May 2014. This total estimate was derived
  from the Tropical Rainfall Monitoring Mission (TRMM) precipitation dataset at a
  spatial resolution of approximately 0.25 degrees for this region. It is possible
  that precipitation levels may have been underestimated for local areas, and is not
  a substitute for ground station measurements.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/geodata-of-estimated-rainfall-accumulation-from-30-april-to-06-may-2014-afgha-may-06-2014]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
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
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: Rainfall accumulation was estimated from TRMM satellite precipitation
    data at 0.25-degree resolution for the period 30 April to 6 May 2014 across Afghanistan.
    UNOSAT analysts processed the satellite-derived precipitation estimates to generate
    spatial maps of total rainfall accumulation. The dataset represents observed precipitation
    patterns derived from satellite remote sensing rather than ground-based measurements.
  sources:
  - id: source_1
    license: null
    name: Tropical Rainfall Monitoring Mission (TRMM)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-estimated-rainfall-accumulation-from-30-april-to-06-may-2014-afgha-may-06-2014
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
  description: Geodata of Estimated Rainfall Accumulation from 30 April to 06 May
    2014, Afghanistan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/AF/FL20140430AFG/FL20140430AFG_shp.zip
  format: null
  id: resource_8223897d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20140430AFG_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Estimated Rainfall Accumulation from 30 April to 06 May
    2014, Afghanistan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/AF/FL20140430AFG/FL20140430AFG.gdb.zip
  format: null
  id: resource_b28d2d56
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20140430AFG.gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-afg_unosat_geodataestimatedrainfalla_20140506
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-05-06'
temporal_resolution: null
title: Geodata of Estimated Rainfall Accumulation from 30 April to 06 May 2014, Afghanistan
version: null
vulnerability: null
---
