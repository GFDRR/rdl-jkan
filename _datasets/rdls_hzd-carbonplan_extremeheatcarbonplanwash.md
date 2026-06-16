---
attributions:
- entity:
    affiliation: null
    email: hello@carbonplan.org
    name: Carbon Plan
    url: https://carbonplan.org/
  id: '0'
  role: author
- entity:
    affiliation: null
    email: null
    name: The Washington Post
    url: https://www.washingtonpost.com
  id: '1'
  role: author
catalog: null
contact_point:
  affiliation: null
  email: pchrzanowski@worldbank.org
  name: Pierre Chrzanowski
  url: null
creator:
  affiliation: null
  email: hello@carbonplan.org
  name: Carbon Plan
  url: https://carbonplan.org/
dataset_id: rdls_hzd-carbonplan_extremeheatcarbonplanwash
description: The final output dataset includes historical and future estimates of
  WBGT in the shade and in the sun for ~15,300 cities and ~24,000 climatically-similar
  regions around the world. The full analysis includes 26 global climate models (GCMs)
  and one emissions scenario (SSP2-4.5). To support different use cases, we've made
  the results available at a few different levels of granularity and in two different
  formats.
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    extreme_temperature:
    - analysis_type: empirical
      calculation_method: inferred
      event_count: 0
      events: []
      frequency_distribution: user_defined
      hazards:
      - classification: null
        id: '0'
        intensity_measure: WBGT:c
        process: extreme_heat
        trigger: null
        type: extreme_temperature
      id: '0'
      occurrence_range: null
      seasonality: user_defined
    - analysis_type: deterministic
      calculation_method: simulated
      event_count: 0
      events: []
      frequency_distribution: user_defined
      hazards:
      - classification: null
        id: '0'
        intensity_measure: WBGT:c
        process: extreme_heat
        trigger: null
        type: extreme_temperature
      id: '1'
      occurrence_range: null
      seasonality: user_defined
    - analysis_type: deterministic
      calculation_method: simulated
      event_count: 0
      events: []
      frequency_distribution: user_defined
      hazards:
      - classification: null
        id: '0'
        intensity_measure: WBGT:c
        process: extreme_heat
        trigger: null
        type: extreme_temperature
      id: '2'
      occurrence_range: null
      seasonality: user_defined
  event_sets_count: 3
license: CC-BY-4.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project:
  name: Modeling extreme heat in a changing climate
  url: null
publisher:
  affiliation: null
  email: null
  name: GFDRR
  url: https://gfdrr.org
purpose: As part of a collaborative project with The Washington Post, we developed
  a new dataset modeling extreme heat under a changing climate.
referenced_by:
- author_names:
  - The Washington Post
  date_published: '2023-09-05'
  doi: null
  id: '0'
  name: Where dangerous heat is surging
  url: https://www.washingtonpost.com/climate-environment/interactive/2023/extreme-heat-wet-bulb-globe-temperature/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time and medians over GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/csv/carbonplan-extreme-heat-annual-maximum-WBGT-shade.csv
  format: csv
  id: '0'
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the shade annual maximum
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time and medians over GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/csv/carbonplan-extreme-heat-days-over-29-degC-WBGT-shade.csv
  format: csv
  id: '1'
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the shade days over 29degC
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time and medians over GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/csv/carbonplan-extreme-heat-days-over-30.5-degC-WBGT-shade.csv
  format: csv
  id: '2'
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the shade days over 30.5degC
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time and medians over GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/csv/carbonplan-extreme-heat-days-over-32-degC-WBGT-shade.csv
  format: csv
  id: '3'
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the shade days over 32degC
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time and medians over GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/csv/carbonplan-extreme-heat-days-over-35-degC-WBGT-shade.csv
  format: csv
  id: '4'
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the shade days over 35degC
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time and medians over GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/csv/carbonplan-extreme-heat-heatwave-days-over-29-degC-WBGT-shade.csv
  format: csv
  id: '5'
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the shade heatwave days over 29degC
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time and medians over GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/csv/carbonplan-extreme-heat-heatwave-days-over-30.5-degC-WBGT-shade.csv
  format: csv
  id: '6'
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the shade heatwave days over 30.5degC
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time and medians over GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/csv/carbonplan-extreme-heat-heatwave-days-over-32-degC-WBGT-shade.csv
  format: csv
  id: '7'
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the shade heatwave days over 32degC
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time and medians over GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/csv/carbonplan-extreme-heat-heatwave-days-over-35-degC-WBGT-shade.csv
  format: csv
  id: '8'
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the shade heatwave days over 35degC
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time and medians over GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/csv/carbonplan-extreme-heat-annual-maximum-WBGT-sun.csv
  format: csv
  id: '9'
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the sun annual maximum
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time and medians over GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/csv/carbonplan-extreme-heat-days-over-29-degC-WBGT-sun.csv
  format: csv
  id: '10'
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the sun days over 29degC
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time and medians over GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/csv/carbonplan-extreme-heat-days-over-30.5-degC-WBGT-sun.csv
  format: csv
  id: '11'
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the sun days over 30.5degC
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time and medians over GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/csv/carbonplan-extreme-heat-days-over-32-degC-WBGT-sun.csv
  format: csv
  id: '12'
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the sun days over 32degC
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time and medians over GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/csv/carbonplan-extreme-heat-days-over-35-degC-WBGT-sun.csv
  format: csv
  id: '13'
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the sun days over 35degC
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time and medians over GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/csv/carbonplan-extreme-heat-heatwave-days-over-29-degC-WBGT-sun.csv
  format: csv
  id: '14'
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the sun heatwave days over 29degC
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time and medians over GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/csv/carbonplan-extreme-heat-heatwave-days-over-30.5-degC-WBGT-sun.csv
  format: csv
  id: '15'
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the sun heatwave days over 30.5degC
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time and medians over GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/csv/carbonplan-extreme-heat-heatwave-days-over-32-degC-WBGT-sun.csv
  format: csv
  id: '16'
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the sun heatwave days over 32degC
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time and medians over GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/csv/carbonplan-extreme-heat-heatwave-days-over-35-degC-WBGT-sun.csv
  format: csv
  id: '17'
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the sun heatwave days over 35degC
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Daily projections for the full ensemble of GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/zarr/daily/historical-WBGT-shade.zarr
  format: Zarr
  id: '18'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the shade historical
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Daily projections for the full ensemble of GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/zarr/daily/ssp245-2030-WBGT-shade.zarr
  format: Zarr
  id: '19'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the shade ssp2-4.5 (2020-2039)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Daily projections for the full ensemble of GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/zarr/daily/ssp245-2050-WBGT-shade.zarr
  format: Zarr
  id: '20'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the shade ssp2-4.5 (2040-2059)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Daily projections for the full ensemble of GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/zarr/daily/historical-WBGT-sun.zarr
  format: Zarr
  id: '21'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the sun historical
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Daily projections for the full ensemble of GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/zarr/daily/ssp245-2030-WBGT-sun.zarr
  format: Zarr
  id: '22'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the sun ssp2-4.5 (2020-2039)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Daily projections for the full ensemble of GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/zarr/daily/ssp245-2050-WBGT-sun.zarr
  format: Zarr
  id: '23'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the sun ssp2-4.5 (2040-2059)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time for the full ensemble of GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/zarr/summaries/historical-summaries-WBGT-shade.zarr
  format: Zarr
  id: '24'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the shade annual maxima, days over threshold historical
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time for the full ensemble of GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/zarr/summaries/historical-summaries-heatwaves-WBGT-shade.zarr
  format: Zarr
  id: '25'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the shade heatwave days ssp2-4.5 (2020-2039)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time for the full ensemble of GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/zarr/summaries/ssp245-2030-summaries-WBGT-shade.zarr
  format: Zarr
  id: '26'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the shade annual maxima, days over threshold ssp2-4.5 (2040-2059)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time for the full ensemble of GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/zarr/summaries/ssp245-2030-summaries-heatwaves-WBGT-shade.zarr
  format: Zarr
  id: '27'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the shade heatwave days historical
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time for the full ensemble of GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/zarr/summaries/ssp245-2050-summaries-WBGT-shade.zarr
  format: Zarr
  id: '28'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the shade annual maxima, days over threshold ssp2-4.5 (2020-2039)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time for the full ensemble of GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/zarr/summaries/ssp245-2050-summaries-heatwaves-WBGT-shade.zarr
  format: Zarr
  id: '29'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the shade heatwave days ssp2-4.5 (2040-2059)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time for the full ensemble of GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/zarr/summaries/historical-summaries-WBGT-sun.zarr
  format: Zarr
  id: '30'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the sun annual maxima, days over threshold historical
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time for the full ensemble of GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/zarr/summaries/historical-summaries-heatwaves-WBGT-sun.zarr
  format: Zarr
  id: '31'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the sun heatwave days ssp2-4.5 (2020-2039)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time for the full ensemble of GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/zarr/summaries/ssp245-2030-summaries-WBGT-sun.zarr
  format: Zarr
  id: '32'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the sun annual maxima, days over threshold ssp2-4.5 (2040-2059)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time for the full ensemble of GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/zarr/summaries/ssp245-2030-summaries-heatwaves-WBGT-sun.zarr
  format: Zarr
  id: '33'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the sun heatwave days historical
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time for the full ensemble of GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/zarr/summaries/ssp245-2050-summaries-WBGT-sun.zarr
  format: Zarr
  id: '34'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the sun annual maxima, days over threshold ssp2-4.5 (2020-2039)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Medians over time for the full ensemble of GCMs
  download_url: https://carbonplan-climate-impacts.s3.us-west-2.amazonaws.com/extreme-heat/v1.0/outputs/zarr/summaries/ssp245-2050-summaries-heatwaves-WBGT-sun.zarr
  format: Zarr
  id: '35'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 5000
  temporal: null
  temporal_resolution: null
  title: WBGT in the sun heatwave days ssp2-4.5 (2040-2059)
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-carbonplan_extremeheatcarbonplanwash
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Extreme Heat - Carbon Plan & The Washington Post
version: null
vulnerability: null
---
