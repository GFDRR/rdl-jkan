---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potential-informal-gathering-sites-over-tanjung-pemenang-districts-indonesia-2838
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potential-informal-gathering-sites-over-tanjung-pemenang-districts-indonesia-2838
dataset_id: rdls_hel-idn_unosat_potentialinformalgatherin_20180809
description: 'This map illustrates satellite-detected potential informal gathering
  sites over Tanjung and Pemenang Districts in Lombok Island, Indonesia as of 8 August
  2018, subsequent to the 6.9 magnitude earthquake, that struck Lombok Island on 5
  August 2018. The analysis was conducted using a post-event Pleiades satellite image
  acquired on 7 and 8 of August 2018. UNITAR-UNOSAT analysis identified about 170
  informal gathering sites in the analysed area of Lombok Island and 6 potential gathering
  sites in Gili Trawangan Island. The size of these temporary gathering sites ranges
  from isolated tents to clusters of tents. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to UNITAR - UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/potential-informal-gathering-sites-over-tanjung-pemenang-districts-indonesia-2838]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Displaced or affected population identified at informal gathering
      sites detected via satellite imagery
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets_by_hazard_type:
    earthquake:
    - analysis_type: probabilistic
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared pre- and post-event Pleiades satellite imagery
    (7-8 August 2018) of Tanjung and Pemenang Districts to identify approximately
    170 informal gathering sites on Lombok Island and 6 sites on Gili Trawangan Island
    as indicators of population displacement following the 5 August 2018 earthquake.
    Site locations and areas were extracted and validated through visual interpretation
    of satellite imagery.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/potential-informal-gathering-sites-over-tanjung-pemenang-districts-indonesia-2838
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement identified through satellite detection of
      informal gathering sites following earthquake
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Potential Informal Gathering Sites over Tanjung & Pemenang Districts,
    Indonesia (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ID/EQ20180805IDN/EQ20180805IDN_shp.zip
  format: null
  id: resource_bd981bd3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20180805IDN_shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-idn_unosat_potentialinformalgatherin_20180809
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-08-09'
temporal_resolution: null
title: Potential Informal Gathering Sites over Tanjung & Pemenang Districts, Indonesia
version: null
vulnerability: null
---
