---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-in-coban-chisec-ixcan-y-sayaxche-municipalities-guatemala-2710
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-in-coban-chisec-ixcan-y-sayaxche-municipalities-guatemala-2710
dataset_id: rdls_hl-gtm_unosat_detectedwaterscobanchisec_20171027
description: 'This map illustrates satellite-detected surface water extent in the
  northern part of Guatemala covering Chisec, Coban Ixcan and Sayaxche municipalities,
  using a Sentinel-1 satellite image acquired on the 09 October 2017. Sentinel-1 imagery
  acquired on 3 and 5 October 2017 was used as pre crisis imagery. UNITAR-UNOSAT analysis
  shows an expansion of water of ~ 4,600 has over the analyzed municipalities, being
  Sayaxche the municipality that was affected the most with an expansion of flood
  waters of ~ 3,200 Ha. The exact limit of flood waters is uncertain because of the
  low spatial resolution of the satellite data used for this analysis. Please send
  ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-waters-in-coban-chisec-ixcan-y-sayaxche-municipalities-guatemala-2710]'
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
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: Sentinel-1 SAR satellite imagery from 3, 5, and 9 October 2017 was
    analyzed by UNOSAT to detect changes in surface water extent. Pre-crisis and post-crisis
    imagery were compared to identify flood water expansion, with results quantified
    as area in hectares per municipality. The dataset represents observed flood extent
    derived from satellite change detection analysis.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-waters-in-coban-chisec-ixcan-y-sayaxche-municipalities-guatemala-2710
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Direct water extent expansion from fluvial flooding measured at approximately
      4,600 hectares across municipalities
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
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
  description: "Satellite Detected Waters in Cob\xE1n, Chisec, Ixc\xE1n y Sayaxch\xE9\
    \ Municipalities, Guatemala (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/GT/FL20171025GTM/FL20171025GTM.gdb.zip
  format: Geodatabase
  id: resource_6eafbfab
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20171025GTM.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Satellite Detected Waters in Cob\xE1n, Chisec, Ixc\xE1n y Sayaxch\xE9\
    \ Municipalities, Guatemala (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/GT/FL20171025GTM/FL20171025GTM.shp.zip
  format: null
  id: resource_d60c78e6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20171025GTM.shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-gtm_unosat_detectedwaterscobanchisec_20171027
spatial:
  bbox: null
  centroid: null
  countries:
  - GTM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-10-27'
temporal_resolution: null
title: "Satellite Detected Waters in Cob\xE1n, Chisec, Ixc\xE1n y Sayaxch\xE9 Municipalities,\
  \ Guatemala"
version: null
vulnerability: null
---
