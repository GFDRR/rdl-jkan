---
attributions:
- entity:
    affiliation: null
    email: null
    name: Climate Hazards Center, UC Santa Barbara
    url: https://data.humdata.org/dataset/historical-dry-spells-in-malawi
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/historical-dry-spells-in-malawi
creator:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/historical-dry-spells-in-malawi
dataset_id: rdls_hzd-mwi_hdx_historicaldryspells_2000
description: 'This dataset includes all the dry spells and rainy seasons in Malawi
  from 2000 till 2021 per admin2. In this dataset a dry spell is defined as 14 consecutive
  days with no more than 2 millimetres of cumulative rainfall. This dataset was produced
  as part of OCHA''s Anticipatory Action pilot in Malawi.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/historical-dry-spells-in-malawi]'
details: The limitations and choice for data sources is described in detail [here](https://ocha-dap.github.io/pa-anticipatory-action/analyses/mwi/docs/mwi_historical_dry_spells_description.html).
  It is highly recommended to read this document before using the data. The code which
  was used to produce this dataset can be found [here](https://github.com/OCHA-DAP/pa-anticipatory-action/blob/1c396ee5367c81ab8ed115bec6ece4ac45b3bd76/analyses/mwi/dryspells_trigger/01_chirps_dry_spell_detection.R)
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
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "Observational rainfall data from Climate Hazards Center was analyzed\
    \ to identify dry spells defined as 14 consecutive days with cumulative rainfall\
    \ \xE2\u2030\xA42mm. Dry spell and rainy season events were catalogued for all\
    \ admin2 divisions in Malawi from 2000-2021 as part of OCHA's Anticipatory Action\
    \ pilot."
  sources:
  - id: source_1
    license: null
    name: Climate Hazards Center, UC Santa Barbara
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/historical-dry-spells-in-malawi
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Includes all the dry spells in Malawi from 2000 till 2021 per admin2.
    This historical dataset was produced as part of OCHA''s Anticipatory Action pilot
    in Malawi. A dry spell is defined as at least 14 consecutive days with a cumulative
    rainfall of no more than 2 mm during the rainy season in an admin2 region. The
    dry spells are determined by using the CHIRPS dataset, which is raster data. This
    raster data was aggregated to admin2 by taking the mean value across all raster
    cells within an admin2. Description of columns: pcode: pcode of the admin2, retrieved
    from the COD administrative boundaries ADM2_EN: name of the admin2, retrieved
    from the COD administrative boundaries Season_name: the start year of the rainy
    season. not during a rainy season indicates dates that are outside the rainy season,
    according to the dates indicated in the rainy_seasons_detail_2000_2021_mean_back.csv.
    NA indicates the onset or cessation date of the rainy season is unknown. Dry_spell_first_date:
    the first day of the dry spell Dry_spell_last_date: the last day of the dry spell
    Dry_spell_duration: the number of days the dry spell lasted. Dry_spell_rainfall:
    total rainfall in millimeters during the dry spell. The cumulative rainfall during
    14 consecutive days is computed on a rolling basis. This can cause the total rainfall
    to be more than 2mm, but during any 14 day period it is not more than 2mm. During_rainy_season:
    binary variable indicating if the 14th day of the dry spell is within the admin2''s
    rainy season, according to the dates indicated in the rainy_seasons_detail_2000_2021_mean_back.csv.
    NA indicates the onset or cessation date of the rainy season is unknown and it
    is therefore unknown whether the dry spell occurred during the rainy season.'
  download_url: https://data.humdata.org/dataset/df68065d-704c-4556-b111-394df000cee4/resource/951c0454-23ab-4057-a7fb-7cfeed4f842d/download/full_list_dry_spells_2000_2021.csv
  format: null
  id: resource_951c0454
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: full_list_dry_spells_2000_2021.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Indicates the start and end of the rainy season in Malawi from 2000
    till 2021 per admin2. This historical dataset was produced as part of OCHA''s
    Anticipatory Action pilot in Malawi. The rainy season onset is defined as the
    first day of a period after 1 Nov with at least 40mm of rain over 10 days AND
    no 10 consecutive days with no more than 2mm of total rain in the following 30
    days. The rainy cessation is the last day before a 15-day period after 15 March
    with 25mm or less of rain. The rainy seasons are determined using the CHIRPS dataset,
    which is raster data. This raster data was aggregated to admin2 by taking the
    mean value across all raster cells within an admin2. Description of columns: pcode:
    pcode of the admin2, retrieved from the COD administrative boundaries ADM2_EN:
    name of the admin2, retrieved from the COD administrative boundaries Season_approx:
    the start year of the rainy season. Onset_date: the start date of the rainy season
    according to the definition described above. NA indicates that the onset_date
    fell in a period that the dataset did not cover . This is the case for the season
    starting in 1999 since the months of October-December 1999 are not included in
    this 2000-2020 dataset. Onset_month: the month of the onset_date Cessation_date:
    the end date of the rainy season according to the definition described above.
    A indicates that the cessation_date fell in a period that the dataset did not
    cover. Cessation_month: the month of the cessation_date. Rainy_season_duration:
    the number of days between onset_date and cessation_date. Rainy_season_rainfall:
    the total rainfall in millimeters between onset_date and cessation_date.'
  download_url: https://data.humdata.org/dataset/df68065d-704c-4556-b111-394df000cee4/resource/0432687f-c9ac-4af0-b894-65ee92105b10/download/rainy_seasons_detail_2000_2021_mean_back.csv
  format: null
  id: resource_0432687f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rainy_seasons_detail_2000_2021_mean_back.csv
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mwi_hdx_historicaldryspells_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - MWI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-05-31'
  start: '2000-01-01'
temporal_resolution: null
title: Historical dry spells in Malawi
version: null
vulnerability: null
---
