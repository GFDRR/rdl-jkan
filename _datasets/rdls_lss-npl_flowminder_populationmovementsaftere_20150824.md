---
attributions:
- entity:
    affiliation: null
    email: null
    name: Flowminder
    url: https://data.humdata.org/dataset/population-movements-after-the-nepal-earthquake-v5-up-to-19th-aug-2015
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Flowminder (inactive)
  url: https://data.humdata.org/dataset/population-movements-after-the-nepal-earthquake-v5-up-to-19th-aug-2015
creator:
  affiliation: null
  email: null
  name: Flowminder (inactive)
  url: https://data.humdata.org/dataset/population-movements-after-the-nepal-earthquake-v5-up-to-19th-aug-2015
dataset_id: rdls_lss-npl_flowminder_populationmovementsaftere_20150824
description: 'Data on abnormal population movements due to the Nepal earthquake of
  April 2015. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/population-movements-after-the-nepal-earthquake-v5-up-to-19th-aug-2015]'
details: 'Mobile phone use is relatively lower in several groups including women,
  children, the elderly, and the poorest. If these groups have substantially different
  movement patterns than groups with high mobile phone use, results will be biased.
  In general the relative distributions of flows across the country are more reliable
  than absolute numbers given per area. Both types of estimates will improve over
  time with additional data. Our previous field projects in Haiti and Kenya show that
  overall estimates of mobility corresponded well to population-level data [1-2],
  but the estimates provided here should be interpreted with the above mentioned caveats
  in mind. [1] Bengtsson et al. (2011) Improved response to disasters and outbreaks
  with mobile phone data: a post-earthquake geospatial study of Haiti [2] Wesolowski
  et al. (2013) The impact of biases in mobile phone ownership on estimates of human
  mobility'
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Population movement data derived from mobile phone records were analyzed
    to identify above-normal population flows between districts in Nepal following
    the 25 April 2015 earthquake. Inflows to each district were estimated by comparing
    observed migration patterns to baseline conditions, with trends tracked through
    August 2015 to quantify displacement persistence and recovery patterns.
  sources:
  - id: source_1
    license: null
    name: Flowminder
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/population-movements-after-the-nepal-earthquake-v5-up-to-19th-aug-2015
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement and abnormal migration flows following the
      April 2015 Nepal earthquake
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
  url: http://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1001083
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kathmandu Valley is here defined as the districts Kathmandu, Bhaktapur
    and Lalitpur. Numbers refer to data which has been used to produce the map on
    p. 4 in the uploaded pdf report.
  download_url: https://data.humdata.org/dataset/1865be22-392d-4142-988d-4fae06d90f47/resource/4e6f570f-61f4-4ccf-9903-8509c2fe3fcd/download/abovenormalinflowsadmin320082015.csv
  format: null
  id: resource_4e6f570f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: above_normal_inflows_admin3_20_08_2015.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This data was used to make the maps on pages 8, 11, 14, 17, 20, 23,
    26, 29, 32, 35, 38 and 41
  download_url: https://data.humdata.org/dataset/1865be22-392d-4142-988d-4fae06d90f47/resource/548df47d-bd7c-429c-abd5-6fa43bdd1b2a/download/abovenormalinflowsadmin420082015.csv
  format: null
  id: resource_548df47d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: above_normal_inflows_admin4_20_08_2015.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Development of above normal inflows into districts over the course
    of the weeks from mid May until 19 Aug. Used to produce the time series on page
    5.
  download_url: https://data.humdata.org/dataset/1865be22-392d-4142-988d-4fae06d90f47/resource/20d43ad7-be72-43df-9dba-3b527664b8e6/download/inflowstrendsadmin320082105.csv
  format: null
  id: resource_20d43ad7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: inflows_trends_admin3_20_08_2105.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Percentage of peopel who remain away from their home district. Used
    to make time series on page 6 of the report.
  download_url: https://data.humdata.org/dataset/1865be22-392d-4142-988d-4fae06d90f47/resource/ec174258-6d6c-49dd-abcc-60836b9790ed/download/percstillawaytrendsadmin320082015.csv
  format: null
  id: resource_ec174258
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: perc_still_away_trends_admin3_20_08_2015.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Percentage of people who remian away from their home VDC. Used to make
    such as the one on page 9 of the report.
  download_url: https://data.humdata.org/dataset/1865be22-392d-4142-988d-4fae06d90f47/resource/0512ca0b-8982-4e33-ae69-dcfb23b59497/download/percstillawayadmin420082015.csv
  format: null
  id: resource_0512ca0b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: perc_still_away_admin4_20_08_2015.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-npl_flowminder_populationmovementsaftere_20150824
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-08-24'
temporal_resolution: null
title: Population movements after the nepal Earthquake v5 up to 19th Aug 2015
version: null
vulnerability: null
---
