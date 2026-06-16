---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/wildfires-in-al-haffa-and-al-qardaha-districts-lattakia-governorate-syria
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/wildfires-in-al-haffa-and-al-qardaha-districts-lattakia-governorate-syria
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/wildfires-in-al-haffa-and-al-qardaha-districts-lattakia-governorate-syria
dataset_id: rdls_hzd-syr_unosat_wildfiresalhaffaalqardaha_20191023
description: 'UNOSAT code: FR20191016LBN This map illustrates satellite-detected burned
  areas in Al-Haffa and Al-Qardaha Districts, Lattakia Governorate, Syria, based on
  SPOT-6 imagery acquired on 21 October 2019. Approximately 433 ha of potentially
  burned areas were detected by UNOSAT as of 21 October 2019 (red). This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR - UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/wildfires-in-al-haffa-and-al-qardaha-districts-lattakia-governorate-syria]'
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
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed SPOT-6 satellite imagery acquired on 21 October
    2019 and compared it with reference imagery to detect notable changes indicative
    of burned areas. Burned polygons were delineated and quantified by area (433 ha)
    as a preliminary field-unvalidated analysis of wildfire extent in Lattakia Governorate,
    Syria.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wildfires-in-al-haffa-and-al-qardaha-districts-lattakia-governorate-syria
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
  description: Wildfires in Al-Haffa and Al-Qardaha Districts, Lattakia Governorate,
    Syria (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/LB/FR20191016LBN/FR20191016LBN_gdb.zip
  format: Geodatabase
  id: resource_da357569
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20191016LBN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Wildfires in Al-Haffa and Al-Qardaha Districts, Lattakia Governorate,
    Syria (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/LB/FR20191016LBN/FR20191016LBN_SHP.zip
  format: null
  id: resource_be7a7268
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20191016LBN_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-syr_unosat_wildfiresalhaffaalqardaha_20191023
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-10-23'
temporal_resolution: null
title: Wildfires in Al-Haffa and Al-Qardaha Districts, Lattakia Governorate, Syria
version: null
vulnerability: null
---
