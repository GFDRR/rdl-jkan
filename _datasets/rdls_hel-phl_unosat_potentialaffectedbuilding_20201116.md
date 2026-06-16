---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/potential-affected-buildings-impact-caused-by-mudslides-in-daraga-municipality-albay-provi
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potential-affected-buildings-impact-caused-by-mudslides-in-daraga-municipality-albay-provi
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potential-affected-buildings-impact-caused-by-mudslides-in-daraga-municipality-albay-provi
dataset_id: rdls_hel-phl_unosat_potentialaffectedbuilding_20201116
description: 'UNOSAT code: TC20201111PHL This map illustrates satellite-detected mudslide
  extent in the Historical Cagsawa and surrounding in Daraga Municipality, Albay Province,
  Bicol Region, Philippines as observed on Pleiades image acquired on 13th of November
  2020 at 10:47 Local time. About 80 buildings are identified as damaged and 30 as
  potentially damaged. Some roads were also identified as potentially damaged. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/potential-affected-buildings-impact-caused-by-mudslides-in-daraga-municipality-albay-provi]'
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
    description: Building stock in Daraga Municipality classified by damage status
      from mudslide impact
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Road network segments identified as potentially damaged by mudslides
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
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
      intensity_measure: LSI:-
      process: landslide_mudflow
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed Pleiades satellite imagery acquired on 13
    November 2020 over Daraga Municipality to detect mudslide extent in the Historical
    Cagsawa area and surrounding regions. Visual change detection and manual interpretation
    identified damaged and potentially damaged buildings and road segments. This preliminary
    analysis was not field-validated at the time of publication.
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
- href: https://data.humdata.org/dataset/potential-affected-buildings-impact-caused-by-mudslides-in-daraga-municipality-albay-provi
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Direct building damage from mudslide impact: 80 buildings damaged,
      30 potentially damaged'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct infrastructure damage from mudslide impact on road network
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
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
  description: Potential affected buildings & impact caused by mudslides in Daraga
    Municipality, Albay Province, Philippines (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20201111PHL/TC20201111PHL_gdb.zip
  format: Geodatabase
  id: resource_618c5090
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201111PHL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Potential affected buildings & impact caused by mudslides in Daraga
    Municipality, Albay Province, Philippines (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20201111PHL/TC20201111PHL_SHP.zip
  format: null
  id: resource_a21be26f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201111PHL_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-phl_unosat_potentialaffectedbuilding_20201116
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-11-16'
temporal_resolution: null
title: Potential affected buildings & impact caused by mudslides in Daraga Municipality,
  Albay Province, Philippines
version: null
vulnerability: null
---
