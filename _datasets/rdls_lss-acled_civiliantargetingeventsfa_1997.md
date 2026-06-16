---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Armed Conflict Location & Event Data Project (ACLED)
  url: https://data.humdata.org/dataset/civilian-targeting-events-and-fatalities
creator:
  affiliation: null
  email: null
  name: Armed Conflict Location & Event Data Project (ACLED)
  url: https://data.humdata.org/dataset/civilian-targeting-events-and-fatalities
dataset_id: rdls_lss-acled_civiliantargetingeventsfa_1997
description: 'A weekly dataset providing the total number of reported civilian targeting
  events and fatalities broken down by country. Civilian targeting events include
  violence against civilians events and explosions/remote violence events in which
  civilians were directly targeted. Note: These are aggregated data files organized
  by country-year and country-month. To access full event data, please register to
  use the Data Export Tool and API on the ACLED website.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/civilian-targeting-events-and-fatalities]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: ACLED collects and codes conflict event data from multiple open sources
    including news reports, NGO databases, and government records. Civilian targeting
    events are identified and filtered according to ACLED's codebook definitions.
    Fatality counts are derived from source reporting and aggregated by country and
    temporal period (weekly, monthly, annual) to produce this summary dataset.
  sources:
  - id: source_1
    license: null
    name: Armed Conflict Location & Event Data Project (ACLED)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/civilian-targeting-events-and-fatalities
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct fatalities from civilian targeting events including violence
      against civilians and explosions
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Count of civilian targeting events where civilians were directly
      targeted
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://acleddata.com/download/2827
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://acleddata.com/acleddatanew/wp-content/uploads/dlm_uploads/2020/02/FAQs_-ACLED-Fatality-Methodology_2020.pdf
- author_names: null
  date_published: null
  doi: null
  id: reference_3
  name: Methodology documentation
  url: https://acleddata.com/acleddatanew/wp-content/uploads/dlm_uploads/2020/02/FAQs_ACLED-Sourcing-Methodology.pdf
- author_names: null
  date_published: null
  doi: null
  id: reference_4
  name: Methodology documentation
  url: https://acleddata.com/download/4404/
- author_names: null
  date_published: null
  doi: null
  id: reference_5
  name: Methodology documentation
  url: https://acleddata.com/resources/general-guides/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A weekly dataset providing the total number of reported civilian targeting
    events and fatalities broken down by country and month. Civilian targeting events
    include violence against civilians events and explosions/remote violence events
    in which civilians were directly targeted.
  download_url: https://data.humdata.org/dataset/921fe117-7158-437b-943d-94969d545362/resource/fb139931-641f-4428-be77-429972878e19/download/civilian-targeting-events-and-fatalities.xlsx
  format: null
  id: resource_fb139931
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civilian-targeting-events-and-fatalities_as-of-2026-01-23.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-acled_civiliantargetingeventsfa_1997
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
  end: '2026-01-23'
  start: '1997-01-01'
temporal_resolution: null
title: Civilian Targeting Events and Fatalities
version: null
vulnerability: null
---
