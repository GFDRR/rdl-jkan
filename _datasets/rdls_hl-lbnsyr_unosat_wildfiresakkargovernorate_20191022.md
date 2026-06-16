---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/wildfires-in-akkar-governorate-lebanon-tartous-and-homs-governorates-syria
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/wildfires-in-akkar-governorate-lebanon-tartous-and-homs-governorates-syria
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/wildfires-in-akkar-governorate-lebanon-tartous-and-homs-governorates-syria
dataset_id: rdls_hl-lbnsyr_unosat_wildfiresakkargovernorate_20191022
description: 'UNOSAT code: FR20191016LBN This map illustrates satellite-detected burned
  areas in Akkar, Tartous and Homs Governorates, in Lebanon and Syria, based on SPOT-6
  imagery acquired on 21 October 2019. Approximately 549 ha of potentially burned
  areas were detected by UNOSAT as of 21 October 2019 (red). This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR - UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/wildfires-in-akkar-governorate-lebanon-tartous-and-homs-governorates-syria]'
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed SPOT-6 satellite imagery acquired on 21 October
    2019 and compared it with reference imagery to detect notable changes indicative
    of burned areas. Burned areas were digitized and quantified in hectares, producing
    a preliminary post-event damage assessment map of wildfire extent in the Akkar,
    Tartous, and Homs Governorates.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wildfires-in-akkar-governorate-lebanon-tartous-and-homs-governorates-syria
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Direct wildfire damage to natural environment with approximately
      549 hectares of burned area detected
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
  description: Wildfires in Akkar Governorate (Lebanon) Tartous and Homs Governorates
    (Syria). (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/LB/FR20191016LBN/FR20191016LBN_gdb.zip
  format: Geodatabase
  id: resource_edf82dca
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
  description: Wildfires in Akkar Governorate (Lebanon) Tartous and Homs Governorates
    (Syria). (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/LB/FR20191016LBN/FR20191016LBN_SHP.zip
  format: null
  id: resource_5e43ea86
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20191016LBN_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-lbnsyr_unosat_wildfiresakkargovernorate_20191022
spatial:
  bbox: null
  centroid: null
  countries:
  - LBN
  - SYR
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-10-22'
temporal_resolution: null
title: Wildfires in Akkar Governorate (Lebanon) Tartous and Homs Governorates (Syria).
version: null
vulnerability: null
---
